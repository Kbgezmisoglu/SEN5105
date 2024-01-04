import datetime

# Patient class definition
class Patient:
        # Constructor to initialize the patient's details, instance variables for storing patient information
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name              = first_name
        self.middle_name             = middle_name
        self.last_name               = last_name
        self.address                 = address
        self.city                    = city
        self.state                   = state
        self.zip_code                = zip_code
        self.phone_number            = phone_number
        self.emergency_contact_name  = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Getter methods to retrieve patient information
    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip_code(self):
        return self.zip_code

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact_name(self):
        return self.emergency_contact_name
    
    def get_emergency_contact_phone(self):
        return self.emergency_contact_phone

    # Setter methods to update patient information
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city
    
    def set_state(self, state):
        self.state = state
    
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name):
        self.emergency_contact_name = emergency_contact_name
    
    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.emergency_contact_phone = emergency_contact_phone

# Procedure class definition, constructor to initialize procedure details
class Procedure:
    def __init__(self, procedure_name, date, practitioner_name, charges):
        self.procedure_name    = procedure_name
        self.date              = date
        self.practitioner_name = practitioner_name
        self.charges           = charges

    # Getter methods for procedure details
    def get_procedure_name(self):
        return self.procedure_name

    def get_date(self):
        return self.date

    def get_practitioner_name(self):
        return self.practitioner_name

    def get_charges(self):
        return self.charges

    # Setter methods for procedure details
    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name

    def set_date(self, date):
        self.date = date

    def set_practitioner_name(self, practitioner_name):
        self.practitioner_name = practitioner_name

    def set_charges(self, charges):
        self.charges = charges

# Function to get patient information from user input, collecting patient details from user input
def get_patient_info():

    print("Please, enter the patient information:")
    first_name              = input("First Name: ")
    middle_name             = input("Middle Name: ")
    last_name               = input("Last Name: ")
    address                 = input("Address: ")
    city                    = input("City: ")
    state                   = input("State: ")
    zip_code                = input("ZIP Code: ")
    phone_number            = input("Phone Number: ")
    emergency_contact_name  = input("Emergency Contact Name: ")
    emergency_contact_phone = input("Emergency Contact Phone: ")

    return Patient(first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone)

# Main script execution
# Getting patient information
patient = get_patient_info()

# Creating procedure objects with current date and specified details
procedure1 = Procedure("Physical Exam", datetime.date.today(),  "Dr. Irvine",   250)
procedure2 = Procedure("X-Ray",         datetime.date.today(),  "Dr. Jamison",  500)
procedure3 = Procedure("Blood Test",    datetime.date.today(),  "Dr. Smith",    200)

# Printing patient information using getter methods
print(f"\n Patient Information: \n Name: {patient.get_first_name()} {patient.get_middle_name()} {patient.get_last_name()} \n Address: {patient.address}, {patient.city}, {patient.state} {patient.zip_code} \n Phone: {patient.phone_number} \n Emergency Contact: {patient.emergency_contact_name} - {patient.emergency_contact_phone}")

# Initializing variables for total charges and procedure count
total_charges   = 0
procedure_order = 0

# Looping through each procedure and printing details, displaying procedure details, accumulating total charges

for procedure in [procedure1, procedure2, procedure3]:
    procedure_order += 1
    print(f"\n Procedure #{procedure_order}: \n Procedure Name: {procedure.get_procedure_name()} \n Date: {procedure.get_date()} \n Practitioner: {procedure.get_practitioner_name()} \n Charges: ${procedure.get_charges():.2f}")
    total_charges += procedure.get_charges()

# Displaying total charges
print(f"\n Total Charges: ${total_charges:.2f}")
