from django.contrib import admin
from .models import UserProfile
from .models import Banner
# Register your models here.
from .models import EmailVerifyRecord
class UserProfileAdmin(admin.ModelAdmin):
    pass

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'send_type', 'send_time')
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter =  ['title', 'image', 'url', 'index', 'add_time']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Banner, BannerAdmin)