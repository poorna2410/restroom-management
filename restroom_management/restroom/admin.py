from django.contrib import admin
from .models import Restroom, RestroomStatus

@admin.action(description='Mark selected restrooms as cleaned')
def mark_restrooms_as_cleaned(modeladmin, request, queryset):
    for status in queryset:
        status.mark_as_cleaned()

class RestroomStatusAdmin(admin.ModelAdmin):
    list_display = ('restroom', 'date', 'clean', 'cleaned_date', 'next_cleaning_date')
    actions = [mark_restrooms_as_cleaned]

admin.site.register(Restroom)
admin.site.register(RestroomStatus, RestroomStatusAdmin)


