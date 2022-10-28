from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class CategoryServ(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    # def __str__(self):
    #     return self.name


class Service(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('CategoryServ', on_delete=models.CASCADE)
    salons = models.ManyToManyField('Salon')

    # def __str__(self):
    #     return self.title


class Salon(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # def __str__(self):
    #     return self.name


class Auto(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.model} - {self.brand}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


