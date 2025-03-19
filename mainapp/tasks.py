
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from .models import Newsletter, Subscriber

@shared_task
def send_newsletter():
    """Fetch the latest unsent newsletter and send it to all subscribers."""
    # Get the latest unsent newsletter scheduled for sending
    newsletter = Newsletter.objects.filter(sent=False, send_at__lte=now()).first()

    if newsletter:
        subscribers = Subscriber.objects.all()
        if not subscribers:
            return "No subscribers to send to."

        # Prepare email content
        html_content = render_to_string('newsletter.html', {
            'subject': newsletter.subject,
            'content': newsletter.content,
        })
        plain_content = strip_tags(html_content)

        # Send the email to each subscriber
        for subscriber in subscribers:
            email = EmailMultiAlternatives(
                subject=newsletter.subject,
                body=plain_content,
                from_email='from@example.com',
                to=[subscriber.email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

        # Mark the newsletter as sent
        newsletter.sent = True
        newsletter.save()

        return f"Newsletter '{newsletter.subject}' sent to {subscribers.count()} subscribers!"
    
    return "No newsletters to send."


















# from celery import shared_task
# from django.core.mail import send_mail
# from django.utils.timezone import now
# from .models import Newsletter, Subscriber

# @shared_task
# def send_newsletter():
#     """Fetch the latest unsent newsletter and send it to all subscribers."""
#     # Get the latest unsent newsletter scheduled for sending
#     newsletter = Newsletter.objects.filter(sent=False, send_at__lte=now()).first()

#     if newsletter:
#         subscribers = Subscriber.objects.all()
#         if not subscribers:
#             return "No subscribers to send to."

#         # Send the email to each subscriber
#         for subscriber in subscribers:
#             send_mail(
#                 subject=newsletter.subject,
#                 message=newsletter.content,
#                 from_email='sajid6207116@gmail.com',
#                 recipient_list=[subscriber.email],
#                 fail_silently=False,
#             )

#         # Mark the newsletter as sent
#         newsletter.sent = True
#         newsletter.save()

#         return f"Newsletter '{newsletter.subject}' sent to {subscribers.count()} subscribers!"
    
#     return "No newsletters to send."



# from celery import shared_task
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from .models import Subscriber, Newsletter
# from django.core.mail import send_mail


# @shared_task
# def send_newsletter():
#     subscribers = Subscriber.objects.all()
#     for subscriber in subscribers:
#         send_mail(
#             'Your Newsletter',
#             'Here’s your latest newsletter update!',
#             'sajid6207116@gmail.com',
#             [subscriber.email],
#             fail_silently=False,
#         )
#     return "Newsletter sent!"



# @shared_task
# def send_newsletter(newsletter_id):
#     """ Celery task to send newsletter emails with HTML content. """
#     try:
#         newsletter = Newsletter.objects.get(id=newsletter_id)
#         subscribers = Subscriber.objects.filter(is_active=True)

#         # Loop through each active subscriber
#         for sub in subscribers:
#             # Render the HTML email content
#             html_content = render_to_string(
#                 'newsletter.html',
#                 {
#                     'subject': newsletter.subject,
#                     'content': newsletter.content,
#                     'unsubscribe_link': f'http://localhost:8000/unsubscribe/{sub.id}/'
#                 }
#             )
#             # Create a plain text version by stripping tags (for email clients that don't support HTML)
#             text_content = strip_tags(html_content)

#             # Create the email
#             email = EmailMultiAlternatives(
#                 subject=newsletter.subject,
#                 body=text_content,
#                 from_email='sajid6207116@gmail.com',
#                 to=[sub.email]
#             )
#             # Attach the HTML version
#             email.attach_alternative(html_content, "text/html")

#             # Send the email
#             email.send()

#         # Mark the newsletter as sent
#         newsletter.sent = True
#         newsletter.save()

#     except Exception as e:
#         print(f"Error sending newsletter: {e}")
