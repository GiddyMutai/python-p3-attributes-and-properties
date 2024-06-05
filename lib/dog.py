#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    # method to initialize the instance attributes
    def __init__(self, name="Bosco", breed="Africanis"):
        self.name = name
        self.breed = breed
    
    # methods to set and get the name property
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name
        elif not name:
            print("Name must be string between 1 and 25 characters.")
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # methods to set the breed property
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

Tommy = Dog(name="Tommy", breed="Mutina")
print(Tommy.breed)


   
        
