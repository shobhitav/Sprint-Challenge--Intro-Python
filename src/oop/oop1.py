# Write classes for the following class hierarchy:
#
#              [Vehicle]
#               /     \ 
#              /      \  
#             /       \
#            v        v
#  [GroundVehicle]   [FlightVehicle]
#    /    \                   /   \                   
#   /     \                  /    \
#  /      \                 v     \
# v       v          [Airplane]   \
# [Car]   [Motorcycle]            v
#                              [Starship]
#   
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle (Base-Class)
 class Vehicle:
     pass

# Ground Vehicle child class of Vehicle and Super Class of Car and Motorcycle
 class GroundVehicle(Vehicle): 
     pass

#class  Motorcycle is a child class of Ground Vehicle
 class Motorcycle(GroundVehicle):
     pass

#class  Motorcycle is a child class of Ground Vehicle
 class Car(GroundVehicle):
     pass

 # FlightVehicle is child class of Vehicle and Super Class of Airplane
 class FlightVehicle(Vehicle):
     pass   

#  class Airplane is a child class of Flight Vehicle 
 class Airplane(FlightVehicle):
     pass  

# class Starship is a child of FlightVehicle
 class Starship(FlightVehicle):
     pass
           