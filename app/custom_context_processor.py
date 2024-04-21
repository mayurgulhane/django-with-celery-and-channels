from notification_app.models import BroadcastNotification

def notification(request):
    allnotifications = BroadcastNotification.objects.all()
    return {'notification': allnotifications}