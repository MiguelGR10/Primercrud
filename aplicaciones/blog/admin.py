from django.contrib import admin
from aplicaciones.blog.models import categoria, Autor, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriasResource(resources.ModelResource):
    class Meta:
        model = categoria

class categorias(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=("nombre","estado","fecha")
    search_fields=['nombre']
    resources_class = CategoriasResource
    

class autores(admin.ModelAdmin):
    list_display=("nombres","apelldos", "web","correo","estado", "fecha")
    search_fields=("nombres", "apelldos")

class blogs(admin.ModelAdmin):
    list_display=("titulo", "slug", "contenido", "categoria", "estado", "fecha")
    search_fields=("titulo","categoria")



admin.site.register(categoria, categorias)
admin.site.register(Autor, autores)
admin.site.register(Post, blogs)

