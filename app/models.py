import os
from django.db import models

# Create your models here.

class Status(models.Model):
    code = models.CharField("Код", max_length=50, blank=True)
    name = models.CharField("Статус", unique=True, max_length=150, blank=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Статусы' 
        verbose_name = 'Статус' 
        ordering = ['name']

class Product(models.Model):
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    sku = models.CharField("Артикул", max_length=255, null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=11, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус",null=True, blank=True)
    photo = models.ImageField("Основное фото", upload_to='images', null=True, blank=True)
    formats = models.CharField("Форматы файлов", max_length=255, null=True, blank=True)

    @property
    def image(self):
        formats = str(self.formats).split(',')
        path = os.path.splitext(self.photo.path)[0]
        image_d = {
                    "path": path,
                    "formats": formats
                    } 
        return image_d


    def save(self, *args, **kwargs):
        from PIL import Image
        
        file, ext = os.path.splitext(self.photo.path)
        if ext[1:] != 'webp':
            super(Product, self).save(*args, **kwargs)
            file, ext = os.path.splitext(self.photo.path)
            image = Image.open(self.photo.path)
            image = image.convert('RGB')
            image.save(file + '.webp', 'webp')
            self.photo = file + '.webp'
            self.formats = 'webp,' + ext[1:]
        super(Product, self).save(*args, **kwargs)