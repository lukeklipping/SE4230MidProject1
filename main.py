def get_patient_name(appointment):
    return appointment["patient"]["name"]

def get_patient_phone(appointment):
    return appointment["patient"]["phone"]

def get_patient_insurance(appointment):
    return appointment["patient"]["insurance"]

def calculate_consultation_fee(doctor_type):
    if doctor_type == "specialist":
        return 150
    elif doctor_type == "general":
        return 100
    else:
        return 75

def calculate_insurance_discount(fee, insurance):
    if insurance == "premium":
        return fee * 0.30
    elif insurance == "standard":
        return fee * 0.15
    else:
        return 0

def calculate_tax(amount):
    return amount * 0.06

def calculate_facility_fee(amount):
    if amount >= 100:
        return 20
    else:
        return 10

def calculate_final_bill(consultation_fee, insurance_discount, tax, facility_fee):
    return consultation_fee - insurance_discount + tax + facility_fee

def print_patient_info(name, phone, insurance):
    print("Patient:", name)
    print("Phone:", phone)
    print("Insurance:", insurance)

def print_bill(consultation_fee, insurance_discount, tax, facility_fee, final_bill):
    print("Consultation Fee: $", consultation_fee)
    print("Insurance Discount: $", insurance_discount)
    print("Tax: $", tax)
    print("Facility Fee: $", facility_fee)
    print("Final Bill: $", final_bill)

def process_billing(appointment):
    consultation_fee = calculate_consultation_fee(doctor_type)
    insurance_discount = calculate_insurance_discount(consultation_fee, patient_insurance)
    amount_after_discount = consultation_fee - insurance_discount
    tax = calculate_tax(amount_after_discount)
    facility_fee = calculate_facility_fee(amount_after_discount)
    final_bill = calculate_final_bill(consultation_fee, insurance_discount, tax, facility_fee)
    return consultation_fee, insurance_discount, amount_after_discount, tax, facility_fee, final_bill

def extract_patient(appointment):
    patient_name = get_patient_name(appointment)
    patient_phone = get_patient_phone(appointment)
    patient_insurance = get_patient_insurance(appointment)
    doctor_type = appointment["doctor_type"]
    return patient_name, patient_phone, patient_insurance, doctor_type

def display_appointment(patient_name, patient_phone, patient_insurance, consultation_fee, insurance_discount, tax, facility_fee, final_bill):
    print_patient_info(patient_name, patient_phone, patient_insurance)
    print_bill(consultation_fee, insurance_discount, tax, facility_fee, final_bill)


def process_appointment(appointment):
    
    patient_name, patient_phone, patient_insurance, doctor_type = extract_patient(appointment)

    consultation_fee, insurance_discount, amount_after_discount, tax, facility_fee, final_bill = process_billing(appointment)

    display_appointment(patient_name, patient_phone, patient_insurance, consultation_fee, insurance_discount, tax, facility_fee, final_bill)

appointment = {
    "patient": {
        "name": "Maria Johnson",
        "phone": "555-2198",
        "insurance": "standard"
    },
    "doctor_type": "specialist"
}

process_appointment(appointment)