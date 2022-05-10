import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "LOL"

print fun()

for i in range(50):
    print fun()

</code>
This will output:
<code>LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
LOL
Segmentation fault (core dumped)
</code>
I've tested this on both Python 2.7 and 3.5
Is this a bug in ctypes?
EDIT: It seems to be a bug in Python itself.

