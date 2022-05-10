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
for interface in iter(rpc):
    print interface

import time
import sys
import threading

def progress():
    chars = ['-', '\\', '|', '/']
    for ch in chars:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\b')

print('Thread: Starting the important task')
thread = threading.Thread(target=progress)
thread.start()

for i in range(8):
    print('
