import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun():
    return 2

print fun()
</code>
This will print <code>1</code>

UPDATE
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun():
    return 2

print fun()

def fun():
    return 3

print fun()
</code>
This will print <code>2</code> and then <code>3</code>

