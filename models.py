from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String,Date


from database import Database

class Unidades(Database):
    __tablename__= "unidades"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    direccion = Column(String(50))
    cct = Column(String(50))
    email = Column(String(50))
    carreras = Column(String(100))
    


class Registros(Database):
    __tablename__="registros"

    id = Column(Integer, primary_key=True)
    fecha=Column(Date)
    dia1=Column(Integer)
    dia2=Column(Integer)
    dia3=Column(Integer)
    dia4=Column(Integer)
    dia5=Column(Integer)
