import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	r  =  range(10101)
	print "fun getting called"
	return r

AddStartupCode(fun, create_native=0, thread_local=True)
print "hello"
#import os
try:
	#print dir(os)
	print "os loaded", os.getpid()
except Exception as e:
	print e 
#import os
from time import sleep
print "started"
sleep(10)
print "bye"
