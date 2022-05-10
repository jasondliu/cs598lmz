import _struct
# Test _struct.Struct and _struct.unpack_from
#
# PyStructObject has a class member called format, and a tp_new slot.
#
# _struct.Struct.__new__() calls PyType_GenericNew(), which returns a
# PyObject_New(PyStructObject, &Structtype) (see Objects/typeobject.c).
#
# PyStructObject_New() will set the format class member from the format
# parameter passed to PyStructObject_New(), then call PyType_GenericNew(),
# which will call the struct_new slot in the struct_type type object.
#
# struct_new() will call PyType_GenericAlloc(), which will call
# PyObject_Malloc() to allocate the memory for the struct object, then
# call the tp_init slot, which is struct_init().
#
# struct_init() will set the format member, then call
# _struct.calcsize(format), and allocate a buffer of that size.
#
# _struct.calcsize() will call _struct.__calcsize_internal(), which
# will call _struct.PyStruct_
