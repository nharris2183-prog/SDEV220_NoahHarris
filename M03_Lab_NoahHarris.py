################################################################################
#  File: M03_Lab_NoahHarris.py
#  Author: Noah Harris
#  Description:
################################################################################

class Vehicle:
    def __init__(self):
        self.vehicle_type = ""


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""


    def get_user_input(self):
        self.vehicle_type = input("Enter the vehicle type: ")
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the roof type (solid or sun roof): ")


    def display_vehicle(self):
        print("\nVehicle Type: " , self.vehicle_type)
        print("Year: " , self.year)
        print("Make: " , self.make)
        print("Model: " , self.model)
        print("Doors: " , self.doors)
        print("Roof: " , self.roof)


def main():
    car = Automobile()
    car.get_user_input()
    car.display_vehicle()

if __name__ == "__main__":
    main()
