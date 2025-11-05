from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from portal.models import Post

def send_notifications(title, emails):
    send_mail(
        subject="Уведомления по подписке!",
        message=f"Появилась новая публикация '{title}' на портале Таро-24",
        from_email="server@server.ru",
        recipient_list=emails,
    )


@receiver(m2m_changed, sender=Post.category.through)
def notifications_new_post(sender, instance, action, **kwargs):
    if action == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for category in categories:
            subscribers = category.subscribers.all()
            subscribers_emails += [sub.email for sub in subscribers]

        subscribers_emails = set(subscribers_emails)

        send_notifications(instance.title, subscribers_emails)

