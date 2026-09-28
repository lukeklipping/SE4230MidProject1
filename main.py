from dataclasses import dataclass

@dataclass(frozen=True)
class PatientInfo:
    name: str
    phone: str
    insurance: str

def calculate_consultation_fee(doctor_type):
    specialist_rate = 150
    general_rate = 100
    default_rate = 75

    if doctor_type == "specialist":
        return specialist_rate
    elif doctor_type == "general":
        return general_rate
    else:
        return default_rate

def calculate_insurance_discount(fee, insurance):
    premium_rate = 0.3
    standard_rate = 0.15
    
    if insurance == "premium":
        return fee * premium_rate
    elif insurance == "standard":
        return fee * standard_rate
    else:
        return 0

def calculate_tax(amount):
    tax_rate = 0.06
    return amount * tax_rate

def calculate_facility_fee(amount):
    if amount >= 100:
        return 20
    else:
        return 10

def calculate_final_bill(consultation_fee, insurance_discount, tax, facility_fee):
    return consultation_fee - insurance_discount + tax + facility_fee

def print_patient_info(patient):
    print("Patient:", patient.name)
    print("Phone:", patient.phone)
    print("Insurance:", patient.insurance)

def print_bill(consultation_fee, insurance_discount, tax, facility_fee, final_bill):
    print("Consultation Fee: $", consultation_fee)
    print("Insurance Discount: $", insurance_discount)
    print("Tax: $", tax)
    print("Facility Fee: $", facility_fee)
    print("Final Bill: $", final_bill)

def process_billing(doctor_type, patient_insurance):
    consultation_fee = calculate_consultation_fee(doctor_type)
    insurance_discount = calculate_insurance_discount(consultation_fee, patient_insurance)
    amount_after_discount = consultation_fee - insurance_discount
    tax = calculate_tax(amount_after_discount)
    facility_fee = calculate_facility_fee(amount_after_discount)

    return (
        consultation_fee, 
        insurance_discount, 
        tax, 
        facility_fee, 
        calculate_final_bill(consultation_fee, insurance_discount, tax, facility_fee) 
    )

def extract_appointment_details(appointment):
    patient = PatientInfo(
        name=appointment["patient"]["name"],
        phone=appointment["patient"]["phone"],
        insurance=appointment["patient"]["insurance"],
    )
    return patient, appointment["doctor_type"]

def display_appointment(patient, consultation_fee, insurance_discount, tax, facility_fee, final_bill):
    print_patient_info(patient)
    print_bill(consultation_fee, insurance_discount, tax, facility_fee, final_bill)


def process_appointment(appointment):
    patient, doctor_type = extract_appointment_details(appointment)

    consultation_fee, insurance_discount, tax, facility_fee, final_bill = process_billing(doctor_type, patient.insurance)

    display_appointment(patient, consultation_fee, insurance_discount, tax, facility_fee, final_bill)

appointment = {
    "patient": {
        "name": "Maria Johnson",
        "phone": "555-2198",
        "insurance": "standard"
    },
    "doctor_type": "specialist"
}

process_appointment(appointment)