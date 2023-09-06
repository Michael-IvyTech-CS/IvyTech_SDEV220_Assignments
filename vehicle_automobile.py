"""
Name vehicle_automobile
Author: Michael Barthaeur
Date: 9/5/2023
Description: Accepts data describing a particular vehicle and it in a class
before printing the vehicle data to the console.
"""


class Vehicle:

    def __init__(self, vehicle_type="car"):
        self.type = vehicle_type


class Automobile(Vehicle):

    def __init__(self, auto_year, auto_make, auto_model, auto_num_doors, auto_roof_type):
        super().__init__()
        self.year = auto_year
        self.make = auto_make
        self.model = auto_model
        self.doors = auto_num_doors
        self.roof = auto_roof_type


print("Please enter the following information about your car.")
# input
year = input("Year: ")  # probably entered as an integer but technically the program doesn't care
make = input("Make: ")
model = input("Model: ")
num_doors = input("Number of doors (2 or 4): ")
roof_type = input("Does your car have a sun roof? (y/n): ").lower()

# determine number of doors
if num_doors.strip() == '2':
    num_doors = 2
else:
    num_doors = 4

# determine roof type
if roof_type == 'y' or roof_type == "yes":
    roof_type = "sun roof"
else:
    roof_type = "solid"

# instantiate car
car = Automobile(year, make, model, num_doors, roof_type)

# output
print("Vehicle Information")
print(f"Vehicle type: {car.type}\nYear: {car.year}\nMake: {car.make}\nModel: {car.model}\n\
Number of doors: {car.doors}\nType of roof: {car.roof}")
