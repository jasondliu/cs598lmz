import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def mycallback(a, b):
   print "in callback, a: %s b: %s" % (a, b)

callback = FUNTYPE(mycallback)

# Call Rust
print "in python, about to call rust"
rust.calculate_factorial(10, callback)
print "in python, after call to rust"
</code>
I get this error:
<code>$ ./test.py
in python, about to call rust
in callback, a: 10 b: 1
in callback, a: 10 b: 2
in callback, a: 10 b: 3
in callback, a: 10 b: 4
in callback, a: 10 b: 5
Traceback (most recent call last):
  File "./test.py", line 15, in &lt;module&gt;
    rust.calculate_factorial(10, callback)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know
 how to convert parameter
