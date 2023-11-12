################################################################################
#  File: M03_Lab_NoahHarris.py
#  Author: Noah Harris
#  Description: This app prompts a user to enter information about a vehicle
#  and then displays the information back to the user. The class Vehicle stores
#  the vehicle type and the class Automobile inherits from Vehicle and stores
#  the year, make, model, number of doors, and roof type. The main function
#  calls the other functions to get the user input and display the vehicle
#  information.
################################################################################

# create class for vehicle
class Vehicle:
    def __init__(self):
        self.vehicle_type = ""


# create Automobile class that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""


# define a function to get input from user and store it 
    def get_user_input(self):
        self.vehicle_type = input("Enter the vehicle type: ")
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the roof type (solid or sun roof): ")


# define a function to display the vehicle information entered by the user
    def display_vehicle(self):
        print("\nVehicle Type: " , self.vehicle_type)
        print("Year: " , self.year)
        print("Make: " , self.make)
        print("Model: " , self.model)
        print("Doors: " , self.doors)
        print("Roof: " , self.roof)


# define main function to call the other functions
def main():
    car = Automobile()
    car.get_user_input()
    car.display_vehicle()

if __name__ == "__main__":
    main()
