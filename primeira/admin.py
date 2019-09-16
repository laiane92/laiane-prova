from django.contrib import admin

# Register your models here.
from . models import Produto

admin.site.register(Produto)

from . models import Cliente

admin.site.register(Cliente)