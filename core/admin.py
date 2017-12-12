from django.contrib import admin

# Register your models here.
from core.models import Accounts, Comments, Photos

admin.site.register(Accounts)
admin.site.register(Comments)
admin.site.register(Photos)