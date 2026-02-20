from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    RESOLVED = 'RESOLVED', 'Resolved'
    CLOSED = 'CLOSED', 'Closed'

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices= TicketStatus.choices,
        default = TicketStatus.OPEN 
    )
    created_at = models.DateTimeField(auto_now_add = True)
    progress = models.IntegerField(default=0)
    assigned_to = models.ForeignKey(User, 
        on_delete = models.SET_NULL,
        null = True, 
        blank = True,
        related_name="assigned_tickets")

    def save(self, *args, **kwargs):
        if self.status == TicketStatus.OPEN:
            self.progress = 0

        elif self.status == TicketStatus.RESOLVED:
            self.progress = 100
        elif self.status == TicketStatus.CLOSED:
            self.progress = 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title