from command import ConcreteCommand, Receiver


def client_code(command):
    command.execute()

# Creamos un objeto de comando
command = ConcreteCommand(Receiver())

# Usamos el comando
client_code(command)