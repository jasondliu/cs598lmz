fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: <generator object <genexpr> at 0x7f22f818d3e8> is not a code object

# The reason is that the __code__ attribute of a function is supposed to be
# of type 'code'.  It is not allowed to be of any other type.

# -------------------------------------------------------------------

# TypeError: expected str, bytes or os.PathLike object, not int

# The reason is that you are not using the right type of object.

# -------------------------------------------------------------------

# TypeError: 'int' object is not subscriptable

# The reason is that you are trying to subscript an int.

# -------------------------------------------------------------------

# TypeError: 'NoneType' object is not callable

# The reason is that you are trying to call a None object.
