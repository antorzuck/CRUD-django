from django.db import models

class Girlfriend(models.Model):
	name = models.TextField()
	number = models.CharField(max_length=12)
	age = models.CharField(max_length=2)
	
	def __str__(self):
		return self.name
