import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) #FUNTYPE = type of the callback

print "create callback object"
callback = FUNTYPE(lambda x: 2 * x) #create callback object
print "callback =", callback
print "callback(42)", callback(42)

print "create python function"
def pyfun(x):
    print "pyfun(x=%s) called" % x
    return x * 2
print "pyfun =", pyfun
print "pyfun(42)", pyfun(42)

print "use python function as callback"
callback = FUNTYPE(pyfun)
print "callback =", callback
print "callback(42)", callback(42)
</code>
Output:
<code>create callback object
callback = &lt;_CFuncPtrObj_ at 0x933e23c&gt;
callback(42) 84
create python function
pyfun = &lt;function pyfun at 0x933e23c&gt;
pyfun(42) called
pyfun(42) 84
use python function as callback
pyfun(x=
