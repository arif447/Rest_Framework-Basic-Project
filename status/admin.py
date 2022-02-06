from django.contrib import admin
from status.models import Status
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']
    class Meta:
        model = Status
# Register your models here.
admin.site.register(Status,StatusAdmin)



