class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Accessors (getters)
    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    # ... Add other accessors for each attribute

    # Mutators (setters)
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    # ... Add other mutators for each attribute

    # Additional methods can be added as needed

class Procedure:
    def __init__(self, procedure_name, date, practitioner_name, charges):
        self.procedure_name = procedure_name
        self.date = date
        self.practitioner_name = practitioner_name
        self.charges = charges

    # Accessors (getters)
    def get_procedure_name(self):
        return self.procedure_name

    def get_date(self):
        return self.date

    def get_practitioner_name(self):
        return self.practitioner_name

    def get_charges(self):
        return self.charges

    # Mutators (setters)
    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name

    def set_date(self, date):
        self.date = date

    def set_practitioner_name(self, practitioner_name):
        self.practitioner_name = practitioner_name

    def set_charges(self, charges):
        self.charges = charges

    # Additional methods can be added as needed


# Create an instance of the Patient class
patient = Patient("John", "A", "Doe", "123 Main St", "Anytown", "Anystate", "12345", "123-456-7890", "Jane Doe", "098-765-4321")

# Create instances of the Procedure class
procedure1 = Procedure("Physical Exam", "01/01/2024", "Dr. Irvine", 250)
procedure2 = Procedure("X-Ray", "01/02/2024", "Dr. Jamison", 500)
procedure3 = Procedure("Blood Test", "01/03/2024", "Dr. Smith", 200)

# Display patient information
print(f"Patient Information:\nName: {patient.get_first_name()} {patient.get_middle_name()} {patient.get_last_name()}\nAddress: {patient.address}, {patient.city}, {patient.state} {patient.zip_code}\nPhone: {patient.phone_number}\nEmergency Contact: {patient.emergency_contact_name} - {patient.emergency_contact_phone}")

# Display procedure information and calculate total charges
total_charges = 0
for procedure in [procedure1, procedure2, procedure3]:
    print(f"\nProcedure: {procedure.get_procedure_name()}\nDate: {procedure.get_date()}\nPractitioner: {procedure.get_practitioner_name()}\nCharges: ${procedure.get_charges()}")
    total_charges += procedure.get_charges()

print(f"\nTotal Charges: ${total_charges}")

