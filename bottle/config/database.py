# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql://sql12247123:2avexty1ed@sql12.freemysqlhosting.net/sql12247123',isolation_level = 'READ UNCOMMITED')
session_db = sessionmaker()
session_db.configure(bind=engine)
