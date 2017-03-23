from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import permalink
from ckeditor.fields import RichTextField

class Tag(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/%y/%m/%d', blank = False)
    body = RichTextField()
    posted = models.DateField(blank=True, null=True, default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=25, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('post_category', None, { 'slug': self.slug })
