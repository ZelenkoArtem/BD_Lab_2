from datetime import datetime


class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message("2. Show table")
        self.show_message("3. Update row")
        self.show_message("4. Delete row")
        self.show_message("5. Exit")
        choice = input("Select your choice: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1. Patient")
        self.show_message("2. Medication")
        self.show_message("3. Medical record")
        self.show_message("4. Medical specialist")
        self.show_message("5. Specialist record")
        self.show_message("6. Back to menu")
        table = input("Select table: ")
        return table

    def show_patient(self, patient):
        print("\nPatient:")
        for pat in patient:
            print(f"Patient ID: {pat.id}, Full name: {pat.full_name}, Age: {pat.age}, Contact info: {pat.contact_info}")

    def show_medication(self, medication):
        print("\nMedication:")
        for med in medication:
            print(f"Medication ID: {med.id}, Name: {med.name}, Dosage form: {med.dosage_form}, Side effect: {med.side_effect}")

    def show_medical_record(self, medical_record):
        print("\nMedical record:")
        for record in medical_record:
            print(f"Medical record ID: {record.id}, ID patient: {record.id_patient}, Visit date: {record.visit_date}, Diagnosis: {record.diagnosis}, Symptoms: {record.symptoms}")

    def show_medical_specialist(self, medical_specialist):
        print("\nMedical specialist:")
        for specialist in medical_specialist:
            print(f"Medical specialist ID: {specialist.id}, Full name: {specialist.full_name}, Qualification: {specialist.qualification}, Work experience: {specialist.work_experience}, Contact info: {specialist.contact_info}")

    def show_specialist_record(self, specialist_record):
        print("\nSpecialist record:")
        for specialist in specialist_record:
            print(f"Specialist record ID: {specialist.id}, Specialist ID: {specialist.id_specialist}, Record ID: {specialist.id_record}")

    def get_patient_input(self):
        while True:
            try:
                id = input("Enter patient ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Patient ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                full_name = input("Enter full name: ")
                if full_name.strip():
                    break
                else:
                    print("Full name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                age = input("Enter age: ")
                if age.strip():
                    age = int(age)
                    break
                else:
                    print("Age cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                contact_info = input("Enter contact info: ")
                if contact_info.strip():
                    break
                else:
                    print("Contact info cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, full_name, age, contact_info


    def get_medication_input(self):
        while True:
            try:
                id = input("Enter Medication ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medication ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_patient = input("Enter id patient: ")
                if id_patient.strip():
                    id_patient = int(id_patient)
                    break
                else:
                    print("ID patient cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                dosage_form = input("Enter dosage form: ")
                if dosage_form.strip():
                    break
                else:
                    print("Dosage form cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                side_effect = input("Enter side effect: ")
                if side_effect.strip():
                    break
                else:
                    print("Side effect cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, id_patient, name, dosage_form, side_effect


    def get_medical_record_input(self):
        while True:
            try:
                id = input("Enter medical record ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medical record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_patient = input("Enter Patient ID: ")
                if id_patient.strip():
                    id_patient = int(id_patient)
                    break
                else:
                    print("Patient ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                visit_date = input("Enter state visit date (YYYY-MM-DD): ")
                if visit_date.strip():
                    datetime.strptime(visit_date, "%Y-%m-%d")
                    break
                else:
                    print("State visit date cannot be empty.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        while True:
            try:
                diagnosis = input("Enter diagnosis: ")
                if diagnosis.strip():
                    break
                else:
                    print("Diagnosis cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                symptoms = input("Enter symptoms: ")
                if symptoms.strip():
                    break
                else:
                    print("Symptoms cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, id_patient, visit_date, diagnosis, symptoms

    def get_medical_specialist_input(self):
        while True:
            try:
                id = input("Enter medical specialist ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medical specialist ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                full_name = input("Enter full name: ")
                if full_name.strip():
                    break
                else:
                    print("Full name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                qualification = input("Enter qualification: ")
                if qualification.strip():
                    break
                else:
                    print("Qualification cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                work_experience = input("Enter work_experience: ")
                if work_experience.strip():
                    work_experience = int(work_experience)
                    break
                else:
                    print("Work_experience cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                contact_info = input("Enter contact info: ")
                if contact_info.strip():
                    break
                else:
                    print("Contact info cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, full_name, qualification, work_experience, contact_info

    def get_specialist_record_input(self):
        while True:
            try:
                id = input("Enter specialist record ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Specialist record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_specialist = input("Enter specialist ID: ")
                if id_specialist.strip():
                    id_specialist = int(id_specialist)
                    break
                else:
                    print("Specialist ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_record = input("Enter record ID: ")
                if id_record.strip():
                    id_record = int(id_record)
                    break
                else:
                    print("Record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return id, id_specialist, id_record

    def get_patient_id(self):
        while True:
            try:
                id = int(input("Enter patient ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medication_id(self):
        while True:
            try:
                id = int(input("Enter medication ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medical_record_id(self):
        while True:
            try:
                id = int(input("Enter medical record ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medical_specialist_id(self):
        while True:
            try:
                id = int(input("Enter medical specialist ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_specialist_record_id(self):
        while True:
            try:
                id = int(input("Enter specialist record ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number