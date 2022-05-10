import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)

class TestObj:
    def __init__(self, name):
        self.name=name
    def onData(self,data,view,input):
        for i in range(view.numberOfValues):
            print "onData",self.name,data.value[i]

#create a loop
loop=uavcan.NodeStatusBroadcaster_getLoop()

#create a dsdl object and give it a name
dsdl=uavcan.NodeStatusBroadcaster_new(loop,"Test1")

#create a python object
test=TestObj("test")

#test the two objects
print dsdl.getName()
print test.name

#create a runnable function that the c++ object can call
#It calls the python class method and passes in the three parameters
#WARNING!  The C object is holding references to the objects.  Do not delete them
def onDataFunc(data,view,input):
    test.
