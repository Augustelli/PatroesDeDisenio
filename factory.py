class Product:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        pass

class ConcreteProduct1(Product):
    def __init__(self):
        super().__init__("Producto 1")

    def do_something(self):
        print("Estoy haciendo algo como producto 1")

class ConcreteProduct2(Product):
    def __init__(self):
        super().__init__("Producto 2")

    def do_something(self):
        print("Estoy haciendo algo como producto 2")

class Factory:
    @staticmethod
    def create_product(product_type):
        if product_type == "producto1":
            return ConcreteProduct1()
        elif product_type == "producto2":
            return ConcreteProduct2()

