# Function to add a new patient.
def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    
    # Dictionary representing the patient
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    
    # Adding the patient dictionary to the list
    patients.append(patient)
    print("Patient added successfully.")

# Function to display all patients.
def display_patients(patients):
    if not patients:
        print("No patients in the list.")
    else:
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

# Function to search for a patient by name and display their details if found.
def search_patient(patients, name):
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found.")

#function to remove a patient by name.
def remove_patient(patients, name):
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print("Patient removed successfully.")
            return
    print("Patient not found.")

#5.while loop to keep the program running until the user chooses to exit.
def main():
    patients = [] 
    
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient(patients, name)
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient(patients, name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
