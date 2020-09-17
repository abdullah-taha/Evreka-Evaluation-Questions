from django.contrib import admin

# Register your models here.
from .models import *


# models for question1
admin.site.register(Vehicle)
admin.site.register(NavigationRecord)

# models for question2
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(Collection)