from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img_url = models.URLField(null=True)
    slug=models.SlugField(unique=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
    # Generate the slug from the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title
    


 

