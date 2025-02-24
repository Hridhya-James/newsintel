from django.contrib import admin
from .models import News
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)
# Register News model in the admin panel
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'sentiment', 'timestamp')
    search_fields = ('title', 'department', 'sentiment')
    list_filter = ('sentiment', 'department')
