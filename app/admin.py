from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Product)
admin.site.register(models.Awards)
admin.site.register(models.Messages)
admin.site.register(models.Testimonial)
