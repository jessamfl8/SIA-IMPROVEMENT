
from django.db import models


class Reminder(models.Model):

    CATEGORY_CHOICES = [
        ('School', '📚 School'),
        ('Personal', '👤 Personal'),
        ('Work', '💼 Work'),
        ('Family', '🏠 Family'),
        ('Health', '💊 Health'),
        ('Others', '📌 Others'),
    ]

    STATUS_CHOICES = [
        ('Pending', '⏳ Pending'),
        ('Ongoing', '🔄 Ongoing'),
        ('Done', '✅ Done'),
    ]

    reminder_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='School'
    )

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    notes = models.TextField()

    def __str__(self):
        return self.item_name
