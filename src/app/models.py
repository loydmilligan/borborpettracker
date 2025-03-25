from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)
    
    # Relationship to pets
    pets = relationship("Pet", back_populates="owner")

class Pet(Base):
    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    date_of_birth = Column(Date)
    weight = Column(Float)
    
    # Foreign key relationship to owner
    owner_id = Column(Integer, ForeignKey('owners.id'))
    owner = relationship("Owner", back_populates="pets")