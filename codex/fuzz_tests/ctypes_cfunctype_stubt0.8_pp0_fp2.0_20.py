import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>


A:

I don't know if there is a better way. You could use <code>ctypes</code> to get the address of <code>Py_None</code> and then use that as a <code>PyCapsule</code> pointer. It's not entirely safe, but nobody said <code>ctypes</code> would be, and it should work:
<code>import ctypes

_PyCapsule_Type = ctypes.PyCObject_Type
_PyCapsule_IsValid = _PyCapsule_Type.tp_is_gc

_PyCapsule_GetPointer = _PyCapsule_Type.tp_descr_get
_PyCapsule_New = _PyCapsule_Type.tp_new

_PyCapsule_GetName = _PyCapsule_Type.tp_getsets['name'].__get__
_PyCapsule_SetName = _PyCapsule_Type.tp_getsets['name'].__set__
_PyCapsule_
