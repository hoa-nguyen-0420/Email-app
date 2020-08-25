from django.contrib import admin
from django.contrib.auth.models import Group
from mail.models import User, Email
# Register your models here.
admin.site.site_header = 'Email Administration'
class EmailAdmin (admin.ModelAdmin):
    list_display = ('id','subject','user','timestamp')
    list_filter = ('timestamp','user',)

admin.site.register(User)
admin.site.register(Email,EmailAdmin)