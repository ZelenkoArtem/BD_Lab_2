from db import SessionLocal
from models import Patient, Medication, MedicalRecord, MedicalSpecialist, SpecialistRecord

class Model:
    def __init__(self):
        self.db = SessionLocal()

    # Методи для роботи з Patient
    def add_patient(self, id, full_name, age, contact_info):
        new_patient = Patient(id=id, full_name=full_name, age=age, contact_info=contact_info)
        self.db.add(new_patient)
        self.db.commit()

    def get_patient(self):
        return self.db.query(Patient).all()

    def update_patient(self, id, full_name, age, contact_info):
        patient = self.db.query(Patient).filter(Patient.id == id).first()
        if patient:
            patient.full_name = full_name
            patient.age = age
            patient.contact_info = contact_info
            self.db.commit()

    def delete_patient(self, id):
        patient = self.db.query(Patient).filter(Patient.id == id).first()
        if patient:
            self.db.delete(patient)
            self.db.commit()

    # Методи для роботи з Medication
    def add_medication(self, id, id_patient, name, dosage_form, side_effect):
        new_medication = Medication(id=id, id_patient=id_patient, name=name, dosage_form=dosage_form, side_effect=side_effect)
        self.db.add(new_medication)
        self.db.commit()

    def update_medication(self, id, id_patient, name, dosage_form, side_effect):
        medication = self.db.query(Medication).filter(Medication.id == id).first()
        if medication:
            medication.id_patient = id_patient
            medication.name = name
            medication.dosage_form = dosage_form
            medication.side_effect = side_effect
            self.db.commit()

    def get_medication(self):
        return self.db.query(Medication).all()

    def delete_medication(self, id):
        medication = self.db.query(Medication).filter(Medication.id == id).first()
        if medication:
            self.db.delete(medication)
            self.db.commit()

    # Методи для роботи з MedicalRecord
    def add_medical_record(self, id, id_patient, visit_date, diagnosis, symptoms):
        new_record = MedicalRecord(id=id, id_patient=id_patient, visit_date=visit_date, diagnosis=diagnosis, symptoms=symptoms)
        self.db.add(new_record)
        self.db.commit()

    def update_medical_record(self, id, id_patient, visit_date, diagnosis, symptoms):
        record = self.db.query(MedicalRecord).filter(MedicalRecord.id == id).first()
        if record:
            record.id_patient = id_patient
            record.visit_date = visit_date
            record.diagnosis = diagnosis
            record.symptoms = symptoms
            self.db.commit()

    def get_medical_record(self):
        return self.db.query(MedicalRecord).all()

    def delete_medical_record(self, id):
        record = self.db.query(MedicalRecord).filter(MedicalRecord.id == id).first()
        if record:
            self.db.delete(record)
            self.db.commit()

    # Методи для роботи з MedicalSpecialist
    def add_medical_specialist(self, id, full_name, qualification, work_experience, contact_info):
        new_specialist = MedicalSpecialist(id=id, full_name=full_name, qualification=qualification,work_experience=work_experience, contact_info=contact_info)
        self.db.add(new_specialist)
        self.db.commit()

    def update_medical_specialist(self, id, full_name, qualification, work_experience, contact_info):
        specialist = self.db.query(MedicalSpecialist).filter(MedicalSpecialist.id == id).first()
        if specialist:
            specialist.full_name = full_name
            specialist.qualification = qualification
            specialist.work_experience = work_experience
            specialist.contact_info = contact_info
            self.db.commit()

    def get_medical_specialist(self):
        return self.db.query(MedicalSpecialist).all()

    def delete_medical_specialist(self, id):
        specialist = self.db.query(MedicalSpecialist).filter(MedicalSpecialist.id == id).first()
        if specialist:
            self.db.delete(specialist)
            self.db.commit()

    # Методи для роботи з SpecialistRecord
    def add_specialist_record(self, id, id_specialist, id_record):
        new_specialist_record = SpecialistRecord(id=id, id_specialist=id_specialist, id_record=id_record)
        self.db.add(new_specialist_record)
        self.db.commit()

    def update_specialist_record(self, id, id_specialist, id_record):
        specialist_record = self.db.query(SpecialistRecord).filter(SpecialistRecord.id == id).first()
        if specialist_record:
            specialist_record.id_specialist = id_specialist
            specialist_record.id_record = id_record
            self.db.commit()

    def get_specialist_record(self):
        return self.db.query(SpecialistRecord).all()

    def delete_specialist_record(self, id):
        record = self.db.query(SpecialistRecord).filter(SpecialistRecord.id == id).first()
        if record:
            self.db.delete(record)
            self.db.commit()

    def close(self):
        self.db.close()
