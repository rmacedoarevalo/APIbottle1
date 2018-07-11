# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from config.database import Base
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
"""
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
"""
class Usuario(Base):
  __tablename__ = 'usuarios'
  id = Column(Integer,primary_key=True)
  nombre= Column(String)
  sistema_id = Column(Integer, ForeignKey('sistemas.id'))

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
