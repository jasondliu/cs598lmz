import weakref
# Test weakref.ref(x) == weakref.ref(x) with objects that have a custom
# __eq__ method.
# The Python proto for __eq__ is "int PyObject_RichCompare(PyObject
# *o1, PyObject *o2, int opid)".  Given objects a and b, the Python
# interpreter transforms the call a == b into PyObject_RichCompare(a,
# b, Py_EQ), and similarly for other comparison operators.  In ceval.c
# the interpreter calls PyObject_RichCompare():
#  - If both operands are objects (not ints, etc.) it calls the
#    object's tp_richcompare slot as built-in_richcmp in
#    object.c:object_richcompare.
#  - If either operand has a __cmp__ method, it follows a path in
#    ceval.c that eventually calls the operand's tp_compare slot.
# Therefore, in order for __eq__ to be called properly, the logic in
# object_richcompare has to be careful to check only the _first_ of
# a
