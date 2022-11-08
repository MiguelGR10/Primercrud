from django.db import models
from ckeditor.fields import RichTextField

class categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length = 50, null = True, blank = False)
    descrip = models.CharField('Descripcion de la categoria', max_length=150, null = True, blank = False )
    imagen = models.ImageField(upload_to='categorias')
    estado = models.BooleanField('Estdo de la categoria', default = True, null = False, blank = False)
    fecha = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True, null = False, blank = False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombres = models.CharField('Nombres del autor', max_length=100 , null = False, blank = False)
    apelldos = models.CharField('Apellidos del autor', max_length= 100, null = False, blank = False)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Electronico', null = True, blank = True)
    estado = models.BooleanField('Estado del autor')
    fecha = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


    def __str__(self):
        return "{0},{1}".format(self.nombres, self.apelldos)

    #def __str__(self):
        #return "{0}{1}.format(self.apelldos, self.nombres)"


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=110, blank=False, null=False )
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='post')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete = models.CASCADE, related_name='tracks')
    estado = models.BooleanField('Publicacion activ o inactiva', default=True)
    fecha = models.DateField('fecha de creacion', auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'

    

    


