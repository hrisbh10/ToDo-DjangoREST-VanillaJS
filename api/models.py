from django.db import models

# Create your models here.
class Task(models.Model):
	todo = models.TextField()
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.todo