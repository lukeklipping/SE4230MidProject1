from dataclasses import dataclass

@dataclass(frozen=True)
class PatientInfo:
    name: str
    phone: str
    insurance: str

@dataclass(frozen=True)
class BillingRecord:
    patient: PatientInfo
    consultation_fee: float
    insurance_discount: float
    tax: float
    facility_fee: float
    final_bill: float

class BillingCalculator:
    def __init__(self, doctor_type, insurance):
        self.doctor_type = doctor_type
        self.insurance = insurance

        self.consultation_fee = self._calculate_consultation_fee()
        self.insurance_discount = self._calculate_insurance_discount()
        self.amount_after_discount = self.consultation_fee - self.insurance_discount
        self.tax = self._calculate_tax()
        self.facility_fee = self._calculate_facility_fee()
        self.final_bill = self._calculate_final_bill()

    def _calculate_consultation_fee(self):
        specialist_rate = 150
        general_rate = 100
        default_rate = 75

        if self.doctor_type == "specialist":
            return specialist_rate
        elif self.doctor_type == "general":
            return general_rate
        else:
            return default_rate

    def _calculate_insurance_discount(self):
        premium_rate = 0.3
        standard_rate = 0.15

        if self.insurance == "premium":
            return self.consultation_fee * premium_rate
        elif self.insurance == "standard":
            return self.consultation_fee * standard_rate
        else:
            return 0

    def _calculate_tax(self):
        tax_rate = 0.06
        return self.amount_after_discount * tax_rate

    def _calculate_facility_fee(self):
        if self.amount_after_discount >= 100:
            return 20
        else:
            return 10

    def _calculate_final_bill(self):
        return self.consultation_fee - self.insurance_discount + self.tax + self.facility_fee

def print_patient_info(patient):
    print("Patient:", patient.name)
    print("Phone:", patient.phone)
    print("Insurance:", patient.insurance)

def print_bill(record):
    print("Consultation Fee: $", record.consultation_fee)
    print("Insurance Discount: $", record.insurance_discount)
    print("Tax: $", record.tax)
    print("Facility Fee: $", record.facility_fee)
    print("Final Bill: $", record.final_bill)

def extract_appointment_details(appointment):
    patient = PatientInfo(
        name=appointment["patient"]["name"],
        phone=appointment["patient"]["phone"],
        insurance=appointment["patient"]["insurance"],
    )
    return patient, appointment["doctor_type"]

def create_billing_record(appointment):
    patient, doctor_type = extract_appointment_details(appointment)
    billing = BillingCalculator(doctor_type, patient.insurance)

    return BillingRecord(
        patient=patient,
        consultation_fee=billing.consultation_fee,
        insurance_discount=billing.insurance_discount,
        tax=billing.tax,
        facility_fee=billing.facility_fee,
        final_bill=billing.final_bill
    )

def display_appointment(record):
    print_patient_info(record.patient)
    print_bill(record)

def process_appointment(appointment):
    billing_record = create_billing_record(appointment)
    display_appointment(billing_record)

appointment = {
    "patient": {
        "name": "Maria Johnson",
        "phone": "555-2198",
        "insurance": "standard"
    },
    "doctor_type": "specialist"
}

process_appointment(appointment)