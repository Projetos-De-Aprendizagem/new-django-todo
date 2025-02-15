from django.db import models

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.description)