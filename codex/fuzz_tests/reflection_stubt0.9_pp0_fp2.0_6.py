fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi # Overwrite the __code__ attribute of the class instance with a generator.

"""
The class definition is translated into a class object.
The `f_code` attribute was automatically set when the function was defined.
Calling the class instance calls the object stored in `f_code`. This is the generator `gi`.
In this case, its next method is called three times.
"""
fn()
fn()
fn()

"""
When the function definition is executed, a function object is created. It is assigned to the variable `f`
  - The instance of the function object has a `f_code` attribute with a function attribute (bytecode string)
  - The instance of the function object has a `f_globals` attribute with a string with the global functions the function will call
  - The instance of the function object has a `f_locals` attribute with a string with the local variables' values at runtime
"""
f_var_string = f.__code__.co_consts[0]
f_code_string = f.__code__.co_code
f_args_num = f.__code
