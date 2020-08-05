from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserSignupForm)
class UserSignupFormAdmin(admin.ModelAdmin):
	list_display = ['id', 'is_logged_in', 'username', 'password1', 'email', 'u_created_time', 'profile_image']

@admin.register(NoteBookModel)
class NoteBookModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'note_title', 'note_author', 'note_body', 'note_image', 'bg_color', 'text_color', 'create_date']

@admin.register(TrashModel)
class TrashModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'note_title', 'note_author', 'note_body', 'note_image', 'deleted_date']

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'author', 'title', 'body', 'bg_color', 'text_color', 'image', 'posted_date']

@admin.register(Community_users)
class Community_userssAdmin(admin.ModelAdmin):
	list_display = ['id', 'username']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['commented_user', 'commented_post', 'comment', 'commented_date']

