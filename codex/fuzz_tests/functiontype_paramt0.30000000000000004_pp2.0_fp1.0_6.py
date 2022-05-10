from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# FunctionType(code, globals, name, argdefs, closure)

# code: the compiled code object
# globals: the global namespace in which the function is defined
# name: the name of the function
# argdefs: the default argument values
# closure: a tuple of cells that contain bindings for the function's free variables

# code:
# co_argcount: the number of positional arguments (including arguments with default values)
# co_nlocals: the number of local variables used by the function (including arguments)
# co_stacksize: the required stack size (including local variables)
# co_flags: flag bits indicating whether the function uses *args, **kwargs, is a generator, etc.
# co_code: a string representing the sequence of bytecode instructions
# co_consts: a tuple of constants used by the bytecode
# co_names: a tuple containing the names used by the bytecode
# co_varnames: a tuple containing the names of the local variables (starting with the argument names)
# co_filename: the
