from django.contrib import admin
from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite
# Register your models here.


class UserAskAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


# 用户课程学习后台管理器
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


# 用户消息后台管理器
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


# 用户评论后台管理器
class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


# 用户收藏后台管理器
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


# 将后台管理器与models进行关联注册。
admin.site.register(UserAsk, UserAskAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(CourseComments, CourseCommentsAdmin)
admin.site.register(UserFavorite, UserFavoriteAdmin)
