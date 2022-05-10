import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    size = ctypes.c_int

p = shm.Shm()
p.get("/asdfasdf", S(1,2,3,4))
print p.data
</code>
I compiled the shared library with 
<code>gcc -shared -fPIC shm.c -o shm.so
</code>
I have also tried using python to compile and run the extension file.
<code>python setup.py build
python /tmp/py/py/debug/build/ext/asdfasdf.so
</code>
When I run the c program I get the expected output.
<code>1 2 3 4
</code>
When I attempt to call the shared library from python, I get the following error.
<code>python /tmp/py/py/debug/build/ext/asdfasdf.so
Traceback (most recent call last):
  File "/tmp/py/py/debug/build/extensions/asdf
