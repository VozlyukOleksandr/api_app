from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import *

class PostResourse(DjangoResource):
	preparer = FieldsPreparer(fields={
		'id': 'id',
		'text': 'text',
		'author': 'user.username',
		'posted_at': 'posted_at',
		'likes':'likes'	})

	def list(self):
		posts=Post.objects.all()
		return posts

	def create(self):
		return Post.objects.create(
    		text=self.data['text'],
    		author=User.objects.get(username=self.data['author']))

	def delete(self, pk):
		Post.objects.get(id=pk).delete()

	def update(self, pk):
		post = Post.objects.get(id=pk)
		post.text = self.data['text']
		post.save
		return post

class UserResourse(DjangoResource):
	preparer = FieldsPreparer(fields={
		'id': 'id',
		'username': 'username',
		'about': 'about',})

	def list(self):
		return User.objects.all()

	def create(self):
		return User.objects.create(
			username=self.data['username'],
			about=self.data['about'])

	def delete(self,uk):
		User.objects.get(id=uk).delete()

	def update(self, uk):
		user = User.objects.get(id=uk)
		user.username = self.data['username']
		user.about= self.data['about']
		user.save
		return user

