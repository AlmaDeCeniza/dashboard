from .extensions import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms import FileField
from werkzeug.datastructures import FileStorage
from .models import Categoria, Producto

class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    label_columns = { "nombre" : "Nombre",
                    "descripcion": "Descripcion",
                    "imagen_render": "Imagen",
                    "estado": "Estado",
                    "creado_en": "Creado en",
                    "actualizado_en":"Actualizado en"}
    
    list_columns= ["nombre", "descripcion", "estado", "creado_en"]
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen_render", "estado", "creado_en","actualizado_en"]
    search_exclude_columns = ["imagen"]
    
    add_form_extra_fields = {"imagen": FileField("Imagen")}
    edit_form_extra_fields = {"imagen": FileField("Imagen")}
    
    def pre_add(self, item):
        if item.imagen and isinstance(item.imagen, FileStorage):
            item.imagen = item.imagen.read()
    
    def pre_update(self, item):
        if item.imagen and isinstance(item.imagen, FileStorage):
            item.imagen = item.imagen.read()
    
class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    label_columns = { "nombre" : "Nombre",
                    "descripcion": "Descripcion",
                    "precio" : "Precio",
                    "categorias": "Categoria",
                    "imagen_render": "Imagen",
                    "estado": "Estado",
                    "creado_en": "Creado en",
                    "actualizado_en":"Actualizado en"}
    
    list_columns= ["nombre", "precio", "categorias", "estado"]
    add_columns = ["nombre", "descripcion","precio","categorias", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion","precio","categorias", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "imagen_render", "estado", "creado_en","actualizado_en"]
    search_exclude_columns = ["imagen"]
    
    add_form_extra_fields = {"imagen": FileField("Imagen")}
    edit_form_extra_fields = {"imagen": FileField("Imagen")}
    
    def pre_add(self, item):
        if item.imagen and isinstance(item.imagen, FileStorage):
            item.imagen = item.imagen.read()
    
    def pre_update(self, item):
        if item.imagen and isinstance(item.imagen, FileStorage):
            item.imagen = item.imagen.read()
    
appbuilder.add_view(CategoriaModelView, "Categorias", icon="fa-info", category="Configuraciones", category_icon="fa-info")
appbuilder.add_view(ProductoModelView, "Productos", icon="fa-info", category="Configuraciones", category_icon="fa-info")
