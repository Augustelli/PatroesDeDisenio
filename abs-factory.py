from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, type):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self, type):
        if type == "dog":
            return Dog()
        else:
            raise ValueError("Invalid animal type")

class CatFactory(AnimalFactory):
    def create_animal(self, type):
        if type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")
