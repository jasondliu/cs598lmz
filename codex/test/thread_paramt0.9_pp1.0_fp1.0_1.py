import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread: Hello, World!\n')).start()
print('Main: Hello, World!')
print('Main: Some seriously long statement that we want to see')

import grpc
from openconfig_interfaces_pb2 import Interfaces, Interface

host = 'localhost'
port = 11004
channel = grpc.insecure_channel('{}:{}'.format(host, port))
stub = InterfacesStub(channel)
rpc = stub.GetInterfaces(Empty())
