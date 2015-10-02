from django.db import models

# Create your models here.
class ImageModel(models.Model):
	img_name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='upload/')