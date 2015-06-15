# -*- coding: utf-8 -*-
from django.db import models
# from users.models import User

class Post(models.Model):
    class Meta:
        verbose_name = u'게시글'

    title = models.CharField(max_length=50, blank=False)
    # user_id = models.ForeignKey(User)
    content = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def create_post(self, title, user_id): 
    	new_post = Post(title=title, user_id=user_id)

    	return new_post

    def set_content_post(self, post, content):
    	post.content = content

    	return post

    class Admin:
    	pass

class Photo(models.Model):
	class Meta:
		verbose_name = u'제품사진'
	post_id = models.ForeignKey(Post)
	filename = models.CharField(max_length=50, blank=True)
	imagedata = models.ImageField(upload_to=None, max_length=100)

	def create_photo(self, filename):
		new_Photo = Photo(filename = filename)

		return new_Photo

	def set_image(self, photo, image):
		photo.imagedata = image

		return photo

	class Admin:
		pass

class HashTag(models.Model):
	class Meta:
		verbose_name = u'해시태그'
	post_id = models.ForeignKey(Post)
	content = models.CharField(max_length=20, blank=True)

	def create_hashtag(self, post_id, content):
		new_hashtag = HashTag(post_id=post_id, content=content)

		return new_hashtag

	class Admin:
		pass

class Comment(models.Model):
	class Meta:
		verbose_name = u'댓글'
	post_id = models.ForeignKey(Post)
	# user_id = models.ForeignKey(User)
	content = models.CharField(max_length=100, blank=False)
	created_date = models.DateTimeField(auto_now_add=True)


	def create_comment(self, post_id, user_id, content):
		new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
		return new_comment

	class Admin:
		pass