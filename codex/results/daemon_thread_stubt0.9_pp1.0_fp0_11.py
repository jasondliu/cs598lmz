import sys, threading

def run():
    # Create the server, binding to localhost on port 9999
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("192.168.43.106", 8013))
    server.register_introspection_functions()

    # Register a function under a different name
    def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'div').
    class MyFuncs:
        def div(self, x, y):
            return x // y

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()

t = threading.Thread(target=run)
t.start()
time.sleep(1)

def stop():
    # Create an object to represent our server.
    server_url = 'http://192.168.43.106:8013'
    proxy = xmlr
