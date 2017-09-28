from django.contrib import admin

# Register your models here.
from dictionary.models import Account, Word

admin.site.register(Account)
admin.site.register(Word)