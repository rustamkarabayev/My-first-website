from django.contrib import admin

from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Team, TeamAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    search_fields = ['name']
    list_display_links = ['name']


admin.site.register(Review, ReviewAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title']
    search_fields = ['title']
    list_display_links = ['title']


admin.site.register(Services, ServicesAdmin)
