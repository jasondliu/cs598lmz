from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# Code objects can be executed or evaluated with different globals and locals:
# eval(codeobj, globals, locals)
# exec(codeobj, globals, locals)

# The compile() built-in function can also be used to create code objects.
# compile(source, filename, mode[, flags[, dont_inherit]])

# The globals() and locals() functions return the current global and local
# dictionary, respectively, which may be useful to pass around for use by
# exec() or eval().

# The built-in vars() function returns the __dict__ attribute of an object, if
# the object has one.

# The dir() built-in function returns a sorted list of strings containing the
# names defined by a module, class, or instance.

# The getattr(), setattr(), and delattr() functions are used to access and
# modify the attributes of an object.

# The __slots__ class attribute can be used to restrict the set of legal
# attributes for instances of a class.

# The has
