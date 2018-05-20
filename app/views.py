from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import *
from django.shortcuts import render_to_response
from django.middleware.csrf import get_token

#Class Basic Views for API
class PostResourse(DjangoResource):
	preparer = FieldsPreparer(fields={
		'id': 'id',
		'text': 'text',
		'author': 'user.username',
		'posted_at': 'posted_at',
		'likes':'likes'	})
	def is_authenticated(self):
		return True

	def list(self):
		posts=Post.objects.all()
		return posts

	def create(self):
		return Post.objects.create(
    		text=self.data['text'],
    		user=Users.objects.get(username=self.data['author']))

	def delete(self, pk):
		Post.objects.get(id=pk).delete()

	def update(self, pk):
		post = Post.objects.get(id=pk)
		post.text = self.data['about']
		post.save()
		return post

class UserResourse(DjangoResource):
	preparer = FieldsPreparer(fields={
		'id': 'id',
		'username': 'username',
		'about': 'about',})

	def is_authenticated(self):
		return True

	def list(self):
		return Users.objects.all()

	def create(self):
		return Users.objects.create(
			username=self.data['username'],
			about=self.data['about'])

	def delete(self, pk):
		Users.objects.get(id=pk).delete()

	def update(self, pk):
		user = Users.objects.get(id=pk)
		user.username = self.data['username']
		user.save()
		user.about= self.data['about']
		user.save()
		return user


# Views for interface API
def reg(request):
	return render_to_response('reg.html', {'cs':get_token(request)})
def post_(request):
	users=Users.objects.all()
	return render_to_response('form_post.html', {'users':users,'cs':get_token(request)})
def delete(request):
	users = Users.objects.all().order_by('id')
	return render_to_response('delete_user.html', {'users': users, 'cs': get_token(request)})
def delete_p(request):
	posts = Post.objects.all().order_by('id')
	return render_to_response('delete_post.html', {'posts': posts, 'cs': get_token(request)})
def put(request):
	users=Users.objects.all()
	return render_to_response('update user.html', {'users':users,'cs':get_token(request)})
def put_post(request):
	posts=Post.objects.all().order_by('id')
	return render_to_response('post_update.html', {'posts':posts,'cs':get_token(request)})

