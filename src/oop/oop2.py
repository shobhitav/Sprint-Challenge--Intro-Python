# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class Vehicle:
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels


class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels

    def drive(self):
        print("vroooom")


# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init__(self,num_wheels=2):
        super().__init__(num_wheels)
        self.num_wheels=2
    
    def drive(self):
        print("BRAAAP!!")

# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
motorcycle=Motorcycle()
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
motorcycle.drive()


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for val in vehicles:
    val.drive()