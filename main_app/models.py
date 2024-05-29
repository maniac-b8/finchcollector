from django.db import models

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  cons = models.CharField(max_length=100)
  location = models.TextField(max_length=250)
  age = models.IntegerField()

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'
