from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a MySQL
SQLALCHEMY_DATABASE_URL = "mysql://root:1234@localhost/ApiTrivia"

# Crear la instancia del motor (Engine)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear el modelo base
Base = declarative_base()
