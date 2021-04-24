from django.contrib import admin
from .models import Contact
from.models import Feedback
# Register your models here.


@admin.register(Contact)
# this is to view fields in admin panel instead of object
class studentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone']

@admin.register(Feedback)
# this is to view fields in admin panel instead of object
class studentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone']


# other way to register model is 

# admin.site.register(Contact)
# admin.site.register(Feedback)
