from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

class SportsCar(Car):
    def __init__(self, wheels, engine, body):
        self.wheels = wheels
        self.engine = engine
        self.body = body

    def get_wheels(self):
        return self.wheels

    def get_engine(self):
        return self.engine

    def get_body(self):
        return self.body

class CarBuilder(ABC):
    @abstractmethod
    def build_wheels(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def get_car(self):
        pass

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None

    def build_wheels(self):
        self.wheels = ["18-inch alloy wheels"]
        return self

    def build_engine(self):
        self.engine = "V8 engine"
        return self

    def build_body(self):
        self.body = "Coupe body"
        return self

    def get_car(self):
        return SportsCar(self.wheels, self.engine, self.body)


class RegularCarBuilder(CarBuilder):
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None

    def build_wheels(self):
        self.wheels = ["14-inch alloy wheels"]
        return self

    def build_engine(self):
        self.engine = "4-cylinder engine"
        return self

    def build_body(self):
        self.body = "Sedan body"
        return self

    def get_car(self):
        return SportsCar(self.wheels, self.engine, self.body)