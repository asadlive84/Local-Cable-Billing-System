from django.contrib import admin
from users.models import CustomUser
from clients.models import Client, Union, Word
from accounts.models import Account, AccountPackage, Package

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Union)
admin.site.register(Word)
admin.site.register(Account)
admin.site.register(AccountPackage)
admin.site.register(Package)
