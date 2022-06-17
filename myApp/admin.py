from django.contrib import admin
from myApp.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')

admin.site.register(student,studentAdmin)
