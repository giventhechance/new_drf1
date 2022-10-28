from django.contrib import admin

from .models import Category, Product, Service, CategoryServ, Salon, Auto

admin.site.register(Product)
admin.site.register(Category)


class CategoryServAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(CategoryServ, CategoryServAdmin)


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Service, ServiceAdmin)

class SalonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Salon, SalonAdmin)

admin.site.register(Auto)