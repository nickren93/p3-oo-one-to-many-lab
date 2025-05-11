class Owner:
    #pass
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        all_owned_pets = self.pets()
        return sorted(all_owned_pets, key=lambda pet: pet.name)

class Pet:
    #pass
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = Owner("Mike")):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception("Pet type must be one of the following: dog, cat, rodent, bird, reptile, exotic.")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

