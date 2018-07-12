# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float,Blob
from config.database import Base
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

class TipoEstacion(Base):
  __tablename__ = 'tipo_estaciones'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)

class Estacion(Base):
  __tablename__ = 'estaciones'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)
  descripcion = Column(String)
  latitud = Column(Float)
  longitud = Column(Float)
  altura = Column(Float)
  tipo_estacion_id = Column(Integer, ForeignKey('tipo_estaciones.id'))

#Tablas del sql en python
class Usuarios(Base):
  __tablename__ = 'Usuario'
  id = Column(Integer,primary_key=True)
  nombre= Column(String)
  skin = Coluns(Blob)
  id_rep_skins = Column(Integer, ForeignKey('Repositorio_Skins.id'))
  #sistema_id = Column(Integer, ForeignKey('sistemas.id'))

class Seleccionar(Base)
_tablename_ = 'seleccionar'
id = Column(Integer,primary_key=True)
id_usuario = Column(Integer, ForeignKey('Usuario.id'))
id_mapas = Column(Integer, ForeignKey('Mapa.id'))
score = Column(Integer)

class Mapas(Base)
_tablename_ = 'Mapa'
id = Column(Integer,primary_key=True)
id_nivel = Column(Integer,ForeignKey(nivel.id))
foto = Column(Blob)


class Niveles(Base)
_tablename_ = 'Nivel'
id = Column(Integer,primary_key=True)
nombre = Column(String)
numero_monedas = Column(Integer)
numero_letras = Column(Integer)

class Partidas(Base)
_tablename_ = 'Partida'
id = Column(Integer,primary_key=True)
id_nivel = Column(Integer,ForeignKey('Nivel.id'))
progreso_realizado = Column(Integer)
monedas_recolectadas = Column(Integer)
letras_recolectadas = Column(Integer)

class Selector_Partidas(Base)
_tablename_ = 'Selector_Partida'
id = Column(Integer,primary_key=True)
id_usuario = Column(Integer, ForeignKey('Usuario.id'))
id_partida = Column(Integer, ForeignKey('Partida.id'))


class Tienda(Base)
_tablename_ = 'tienda'
id = Column(Integer,primary_key=True)
id_usuario = Column(Integer, ForeignKey('Usuario.id'))
id_rep_skins = Column(Integer, ForeignKey('Repositorio_Skins.id'))
monedas_disponibles = Column(Integer)

class RepositorioSkins(Base)
_tablename_ = 'Repositorio_Skins'
id = Column(Integer,primary_key=True)
id_usuario = Column(Integer, ForeignKey('Usuario.id'))
id_tienda = Column(Integer, ForeignKey('tienda.id'))

"""
class Skins(Base):
  id = Column(Integer, primary_key=True)
  imagen=Column(file)
  nombre=Column(String)
  descripcion= Column(String)
  disponiblidad=Column(Boolean)
  valor = Column(Integer)

class RepositorioSkins_Usuario(Base):
  __tablename__ = 'skins'
  id= Column(Integer,primary_key=True)
  skins= Column({Skins})
  utilizacion = Column(Boolean)
  usuario_id = Column(Integer, ForeignKey('usuarios.id'))

class Partida(Base):
  __tablename__= 'partida'
  id= Column(Integer, primary_key=True)
  monedas = Column(Integer)
  letras = Column(Array[String])
  progreso = Column(Integer)

class ContadorMonedas(Base):
  __tablename__= 'contador'
  id= Column(Integer, primary_key=True)
  contador_Monedas= Column(Integer)
  partida_id = Column(Integer,ForeignKey('partida.id'))

class MonedasFinales(Base):
  __tablename__= 'monedas_finales'
  id= Column(Integer, primary_key=True)
  valor_monedas= Column (Integer)
  validez_monedas= Column(Boolean)
  partida_id = Column(Integer, ForeignKey('partida.id'))

class RepositorioSkins_Tienda(Base):
  __tablename__= 'tienda'
  id= Column(Integer,primary_key=True)
  skins_tienda= Column({Skins})
  cantidad_monedas= Column(Integer)
  usuario_id= Column(Integer, ForeignKey('usuarios.id'))

class ActualizarMonedas_Tienda(Base):
  __tablename__= 'monedas_a_tienda'
  id=Column(Integer,primary_key=True)
  monedas_finales_id= Column(Integer,ForeignKey('monedas_finales.id'))
  tienda_id= Column(Integer,ForeignKey('tienda.id'))
"""

"""
