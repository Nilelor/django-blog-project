from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	body=models.TextField()
	author=models.CharField(max_length=60)
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)
	post=models.ForeignKey(Post)
	def exactBody(self):
		return self.body[:60]
	def __unicode__(self):
		return self.author



class CommentInline(admin.TabularInline):
	model=Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated')
	search_fields = ('title','body')
	list_filter = ('created',)
	inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author','exactBody','created','updated')
	list_filter = ('created','author')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)	
	

