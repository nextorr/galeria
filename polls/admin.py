# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Imagen
from .models import Category
from .models import Media


# Register your models here.
admin.site.register(Imagen)
admin.site.register(Category)
admin.site.register(Media)
