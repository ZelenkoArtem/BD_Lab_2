from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Сутність Пацієнт
class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    contact_info = Column(String, nullable=False)
    medical_records = relationship("MedicalRecord", back_populates="patient", cascade="all, delete-orphan")

# Сутність Медикамент
class Medication(Base):
    __tablename__ = 'medication'
    id = Column(Integer, primary_key=True)
    id_patient = Column(Integer, ForeignKey('patient.id'), nullable=False)
    name = Column(String, nullable=False)
    dosage_form = Column(String, nullable=False)
    side_effect = Column(String)

# Сутність Медична Записка
class MedicalRecord(Base):
    __tablename__ = 'medical_record'
    id = Column(Integer, primary_key=True)
    id_patient = Column(Integer, ForeignKey('patient.id'), nullable=False)
    visit_date = Column(Date, nullable=False)
    diagnosis = Column(Text, nullable=False)
    symptoms = Column(Text, nullable=True)
    patient = relationship("Patient", back_populates="medical_records")

# Сутність Медичний Спеціаліст
class MedicalSpecialist(Base):
    __tablename__ = 'medical_specialist'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    qualification = Column(String, nullable=False)
    work_experience = Column(Integer, nullable=False)
    contact_info = Column(String, nullable=False)
    specialist_records = relationship("SpecialistRecord", back_populates="specialist", cascade="all, delete-orphan")

# Сутність Зв'язок Спеціаліст-Медична Записка
class SpecialistRecord(Base):
    __tablename__ = 'specialist_record'
    id = Column(Integer, primary_key=True)
    id_specialist = Column(Integer, ForeignKey('medical_specialist.id'), nullable=False)
    id_record = Column(Integer, ForeignKey('medical_record.id'), nullable=False)
    specialist = relationship("MedicalSpecialist", back_populates="specialist_records")
    record = relationship("MedicalRecord")
