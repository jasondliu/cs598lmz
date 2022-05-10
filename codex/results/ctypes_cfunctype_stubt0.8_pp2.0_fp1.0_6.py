import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0.5
obj = fun(())
</code>
then the interpreter crashes with
<code>#0  0x0000000000438676 in object_subtype (type=0xc9b510, base=0xdfbba0) at Objects/typeobject.c:611
#1  0x00000000004428fe in instancemethod_new (func=0xc9b510, self=0x0, classObj=0xdfbba0) at Objects/classobject.c:2058
#2  0x00000000004429a9 in PyInstanceMethod_New (func=0xc9b510) at Objects/classobject.c:2092
#3  0x0000000000434e69 in PyObject_CallMethodObjArgs (callable=0xdfbc20, name=0xdfbc68, name=0xdfbc68, arg=0x0, arg=0x0) at Objects/abstract.c:1882
#4  0x0000000000434f54 in PyObject_CallMethod (o=0xdfbd00, name=0xdfbd48
