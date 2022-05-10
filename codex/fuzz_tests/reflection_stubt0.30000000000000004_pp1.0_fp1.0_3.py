fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a bit more complicated.
#
# The __code__ attribute of a function is a code object.  The code object
# contains a pointer to the function's bytecode, and a pointer to the
# function's globals.  The function's globals are a dictionary, and the
# dictionary contains a pointer to the function's code object.  So we have a
# cycle.
#
# The cycle is broken by the garbage collector.  The code object is
# unreachable, so it is collected.  The code object's tp_clear slot is called,
# which sets the code object's globals pointer to NULL.  The code object is
# then freed.  The dictionary is then collected, and the dictionary's
# tp_clear slot is called, which sets the dictionary's code object pointer to
# NULL.  The dictionary is then freed.
#
# The code object's tp_clear slot is implemented in Objects/codeobject.c.
# The dictionary's tp_clear slot is implemented in Objects/dictobject.c.
#
# The code object's tp_clear
