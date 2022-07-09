from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    url=models.URLField()
    image=models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title
