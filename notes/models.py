from django.db import models

LABEL_CHOICES = (("P", "primary"),
                 ("S", "seconda"),
                 ("SU", "success"),
                 ("D", "danger"),)


class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, default='P', max_length=2)

    def __str__(self) -> str:
        return self.title
