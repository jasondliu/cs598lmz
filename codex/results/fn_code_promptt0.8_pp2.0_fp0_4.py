fn = lambda: None
# Test fn.__code__.co_freevars and fn.__closure__
"""
running the above snippet will generate a fn with a closure and a code object that
contains the variable id(x), but the variable isn't in scope any more.

there is nothing in scope by the name 'x', so there is nothing
that can go into fn's closure. But it doesn't matter, because fn's code object
says that the variable is free, and python has to look somewhere to find its value.
So, when the function is called, the missing variable is just set to None.
"""

"""
The __closure__ attribute of the function object is a tuple of cells, which contain
the bindings for the function's free variables. A cell is a simple container that
holds a single value. You can get their contents by calling them.

A cell is used to implement lexical closures because the contents, when
the function is first defined, are unbound local variables. When the function
is later called, the cells contain the values of those variables from the
environment in which the function was called.
"""
fn.__closure__[0].cell_contents
# variable
