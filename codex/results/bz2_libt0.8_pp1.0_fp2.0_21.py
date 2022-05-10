import bz2
bz2.decompress()

import bz2
s = bz2.BZ2File('somefile.bz2')
for line in s:
    ...
    print(line)


#xmlrpclib

import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9000')
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
s.keys()


#xmlrpcclib
import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9000')
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
s.keys()


#xmlrpcclib
#server


import SimpleXMLRPCServer

def set(name, value):
    database[name] = value

def get(name):
    return database[name]
# Make a new server
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 9000))


