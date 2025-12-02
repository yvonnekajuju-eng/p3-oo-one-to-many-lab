class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Must be a Pet instance
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")

        # Assign this owner to the pet
        pet.owner = self

    def get_sorted_pets(self):
        # Return pets sorted alphabetically by name
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        # Validate owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")

        self.owner = owner

        # Track all pets created
        Pet.all.append(self)
