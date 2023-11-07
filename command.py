class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.do_something()

class Receiver:
    def do_something(self):
        print("Estoy haciendo algo")