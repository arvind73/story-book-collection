from django.db import models
# A category and story model used here.
# Create your models here.
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('story:story_category',args=[self.slug])


class Story(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)     #author field
    title = models.CharField(max_length=150)
    body=RichTextField()
    description=models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering=('publish_date',)

    def get_absolute_url(self):
        return reverse('story:story_detail',args=[self.id])
