from factory import Factory


def client_code(factory):
    product = factory.create_product("producto1")
    product.do_something()

factory = Factory()

client_code(factory)