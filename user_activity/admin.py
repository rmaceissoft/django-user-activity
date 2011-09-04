from django.contrib import admin

from user_activity.models import ActivityType


class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('keyname', 'label')

admin.site.register(ActivityType, ActivityTypeAdmin)