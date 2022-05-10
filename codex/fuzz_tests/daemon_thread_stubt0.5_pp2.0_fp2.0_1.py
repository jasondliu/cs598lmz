import sys, threading

def run():
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000))
    server.register_introspection_functions()
    server.register_function(pow)
    server.register_function(lambda x,y: x+y, 'add')
    def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add_func')
    class MyFuncs:
        def div(self, x, y):
            return x // y
    server.register_instance(MyFuncs())
    server.serve_forever()

if __name__ == '__main__':
    run()
