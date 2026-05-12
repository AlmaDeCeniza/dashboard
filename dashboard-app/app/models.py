import datetime
from flask_appbuilder import Model
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.orm import relationship

class Categoria(Model):
    __tablename__="categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(LONGBLOB, nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow ,nullable=False)
    actualizado_en = Column(DateTime, default=datetime.datetime.utcnow, onupdate= datetime.datetime.utcnow, nullable=False)
    
    productos = relationship("Producto", back_populates="categorias")

    @property
    def imagen_render(self):
        if self.imagen:
            # Creamos un link a la ruta /admin/imagen/categoria/ID
            return f'<img src="/admin/imagen/categoria/{self.id}" width="200" style="border-radius:10px;"/>'
        return "Sin imagen"
    
    def __repr__(self):
        return  self.nombre
    
class Producto(Model):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    imagen = Column(LONGBLOB, nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow ,nullable=False)
    actualizado_en = Column(DateTime, default=datetime.datetime.utcnow, onupdate= datetime.datetime.utcnow, nullable=False)
    categorias = relationship("Categoria", back_populates="productos")

    @property
    def imagen_render(self):
        if self.imagen:
            # Creamos un link a la ruta /admin/imagen/producto/ID
            return f'<img src="/admin/imagen/producto/{self.id}" width="200" style="border-radius:10px;"/>'
        return "Sin imagen"

    def __repr__(self):
        return  self.nombre
