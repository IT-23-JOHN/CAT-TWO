#base Vehicle class with attributes registration_number, make, and model.
class Vehicle:
    def __init__(self, registration_number, make, model):
    
        #Initialize a Vehicle object.

    # Registration number of the vehicle.
    #Make of the vehicle.
    #Model of the vehicle.
        
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
    
    # Display basic information about the vehicle.
        
        print(f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}")
#Car, Truck, and Motorcycle classes that inherit from Vehicle and add their respective specific attributes.
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        
        #Initialize a Car object, inheriting from Vehicle.

        # Registration number of the car.
        # Make of the car.
        # Model of the car.
        #Number of seats in the car.
        
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        
        #Display information about the car.
        
        super().display_info()
        print(f"Number of Seats: {self.number_of_seats}")

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        
        #Initialize a Truck object, inheriting from Vehicle.

        # Registration number of the truck.
        # Make of the truck.
        # Model of the truck.
        # Cargo capacity of the truck.
        
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        
        #Display information about the truck.
        
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity} tons")

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        
        #Initialize a Motorcycle object, inheriting from Vehicle.

        # Registration number of the motorcycle.
        # Make of the motorcycle.
        # Model of the motorcycle.
        # Engine capacity of the motorcycle.

        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        
    #Display information about the motorcycle.
    
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity} cc")
#Fleet class to manage the fleet, with methods to add a vehicle, display all vehicles, and search for a vehicle by registration number.
class Fleet:
    def __init__(self):
       
    #Initialize a Fleet object to manage multiple vehicles.
        
        self.vehicles = []

    def add_vehicle(self, vehicle):
    
    #Add a vehicle to the fleet.

    #A Vehicle object (Car, Truck, or Motorcycle).
        
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
    
    #Display information about all vehicles in the fleet.
    
        for vehicle in self.vehicles:
            vehicle.display_info()
            print('-' * 30)

    def search_vehicle_by_registration_number(self, registration_number):
        
        #Search for a vehicle by its registration number.

        # Registration number to search for.
        #return: The vehicle with the matching registration number, or None if not found.
        
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None

#instance of the Fleet class to demonstrate the functionalities.
fleet = Fleet()
# Create different types of vehicles
car = Car("ABC123", "Toyota", "Camry", 5)
truck = Truck("XYZ789", "Volvo", "FH16", 20)
motorcycle = Motorcycle("MNO456", "Yamaha", "R1", 1000)

# Add vehicles to the fleet
fleet.add_vehicle(car)
fleet.add_vehicle(truck)
fleet.add_vehicle(motorcycle)

# Display all vehicles in the fleet
print("Displaying all vehicles in the fleet:")
fleet.display_all_vehicles()

# Search for a vehicle by registration number
print("Searching for vehicle with registration number 'XYZ789':")
found_vehicle = fleet.search_vehicle_by_registration_number("XYZ789")
if found_vehicle:
    found_vehicle.display_info()
else:
    print("Vehicle not found.")
