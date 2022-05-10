import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int)
def my_callback(number):
    print "my_callback called with "+str(number)
    
c_callback = FUNTYPE(my_callback)

s = "hello world"
print "original string is "+s
append_a_c(s,c_callback)
print "now the string is "+s

print "The address of the string object is:",ctypes.addressof(s)

#the problem is that the original string was originally immutable, so we pass in the address of the object to the C library. then the C library makes changes to the object, but CPython does not recognize this.

#the solution is to tell CPython to refresh the string object

c_callback(1)

s = s.decode()
print "now the string is "+s
