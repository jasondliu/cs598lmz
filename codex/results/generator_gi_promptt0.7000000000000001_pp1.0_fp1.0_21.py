gi = (i for i in ())
# Test gi.gi_code.co_flags for the "compiler_flag" enum.
[gi.gi_code.co_flags for gi in ((i for i in ()),)]
# Test gi.gi_code.co_freevars for the "PyObject *" type.
[gi.gi_code.co_freevars for gi in ((i for i in ()),)]
# Test gi.gi_code.co_lnotab for the "PyObject *" type.
[gi.gi_code.co_lnotab for gi in ((i for i in ()),)]
# Test gi.gi_code.co_name for the "const char *" type.
[gi.gi_code.co_name for gi in ((i for i in ()),)]
# Test gi.gi_code.co_names for the "PyObject *" type.
[gi.gi_code.co_names for gi in ((i for i in ()),)]
# Test gi.gi_code.co_nlocals for the "int" type.
[gi.gi_code.
