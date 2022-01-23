from django.contrib import admin
from .models import vegetables,fruits,beverages,babies,bread_bakery
# Register your models here.
admin.site.register(vegetables)
admin.site.register(fruits)
admin.site.register(beverages)
admin.site.register(babies)
admin.site.register(bread_bakery)
