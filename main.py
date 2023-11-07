class Handler:
    def handle(self, request):
        pass

    def set_next(self, handler):
        self.next_handler = handler
class ConcreteHandler1(Handler):
    def handle(self, request):
        if request.type == "tipo1":
            print("Manejador 1 ha manejado la solicitud")
            return True
        else:
            return False

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request.type == "tipo2":
            print("Manejador 2 ha manejado la solicitud")
            return True
        else:
            return False

class Request:
    def __init__(self, type):
        self.type = type

def client_code(chain):
    request = Request("tipo1")
    print("Enviando solicitud...")
    chain.handle(request)


def main():
    chain = ConcreteHandler1()
    chain.set_next(ConcreteHandler2())

    # Usamos la cadena de responsabilidad
    client_code(chain)

if __name__ == "__main__":
    main()