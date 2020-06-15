from django.db import models

# Create your models here.
from Gallery_app import admin


class Art(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=150)
    teacher = models.CharField(max_length=20)
    series = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    size = models.CharField(max_length=10)

    def _str_ (self):
        return self.name, self.author, self.teacher, self.series, self.description, self.description, self.size

# class ArtAdmin(admin.ModelAdmin):
#     list_display = ['name','author','teacher', 'series', 'description', 'size']
#     pass