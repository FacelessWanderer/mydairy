from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='static/images')


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('my_profile')


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=40, default='global')
    like = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)