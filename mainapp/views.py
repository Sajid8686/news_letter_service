from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Newsletter, Subscriber
from .tasks import send_newsletter  # Import the Celery task

# Home page
def index(request):
    return render(request, 'index.html')


# Newsletter creation page (with email sending trigger)
def newsletter(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        if subject and content:
            # Create a new newsletter entry in the database
            newsletter_instance = Newsletter.objects.create(
                subject=subject,
                content=content
            )

            # Trigger the Celery task to send emails
            send_newsletter.delay(newsletter_instance.id)

            return HttpResponse("Newsletter is being sent!")

    return render(request, 'newsletter.html')


def newsletter_dashboard(request):
    newsletters = Newsletter.objects.all().order_by('-created_at')
    subscribers = Subscriber.objects.all()
    
    return render(request, 'newsletter_dashboard.html', {'newsletters': newsletters, 'subscribers': subscribers})


# Unsubscribe link handler
def unsubscribe(request, sub_id):
    """ Handle unsubscribe link from email. """
    subscriber = get_object_or_404(Subscriber, id=sub_id)
    subscriber.is_active = False
    subscriber.save()
    return HttpResponse("You've successfully unsubscribed.")
