# -*- coding: utf-8 -*-
from django.db import models
from users.models import User


class Tag(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Post(models.Model):

    class Meta:
        ordering = ['created_at']

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    comments = models.PositiveSmallIntegerField(default=0, null=True)

    def __unicode__(self):
        return self.title


class Photo(models.Model):

    post = models.ForeignKey(Post, related_name='photos', related_query_name="photo")
    image_file= models.ImageField(upload_to='uploaded')

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        super(Post, self).delete(*args, **kwargs)

    def __unicode__(self):
        return "%s" % (self.id)

class Comment(models.Model):

    post = models.ForeignKey(Post)
    content = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def create_comment(self, post_id, user_id, content):
        new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
        return new_comment

    def __unicode__(self):
        return self.content
