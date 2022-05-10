import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import pickle
pickle.loads(pickle.dumps(range(10)))

import json
json.loads(json.dumps(range(10)))

import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9000')
s.pow(2,3)
s.add(2,3)
s.div(5,2)

from SimpleXMLRPCServer import SimpleXMLRPCServer
def add(x,y):
    return x+y
server = SimpleXMLRPCServer(('localhost',9000))
server.register_function(add,'add')
server.serve_forever()

import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9000')
s.add(2,3)

import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9000',allow_none=True)
s.add(2,3
