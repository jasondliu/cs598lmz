gi = (i for i in ())
# Test gi.gi_code seems to be empty (for some reason setting f_code to None
# causes a segfault in PyObject_GetAttrString during PyDict_SetItem)
Support.compileString("def f(): pass", "")
g
