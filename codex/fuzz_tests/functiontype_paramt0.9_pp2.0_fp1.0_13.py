from types import FunctionType
list(FunctionType(small_script,globals(),'f'))
# Name: f
# Docstring: None
# Type: function

# ----------------------------------------------------------------------------------------------------------
# A program that is running at runtime is called a process.
# IDLE and your system’s command shell are also processes.
# An environment is a collection of objects in process memory, which may include data, state and functions.
# The script passed to the interpreter uses the current process and the global environment.

# ----------------------------------------------------------------------------------------------------------
# Python uses the ‘del’ keyword to remove any specified object.
# If the object is in memory, then it is immediately removed.
# If you are using the implicit name, then you must refer to the function using a name, such as ‘idle’.
# Remember: IDLE may be running several scripts at the same time. Any of them may be using the implicit name.
del small_script
# If you try to use ‘small_script’, or ‘f’, then the interpreter will raise a NameError exception.
small_script
# Traceback (most recent call last):
#   File "<pys
