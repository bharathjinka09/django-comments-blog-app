from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish', 'allow_comments')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']
    fieldsets = ((None,
                  {'fields': ('title', 'slug', 'body',  'status',
                              'allow_comments', 'publish',)}),)
