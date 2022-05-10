import ctypes
ctypes.cast(l1[0], ctypes.py_object).value

# In the current implementation, only one line of code at a time can be executed by a Python interpreter. 
# For example, calling exec or eval does not immediately return but waits for the results to be ready.
# However, since there is at most one thread of control within the Python interpreter, 
# there is no need to provide any special synchronization primitives.

# The only difference is that the PyPy interpreter executes a stackless bytecode. 
# No stack frame is allocated for function calls, but rather a C-like continuation passing style 
# is used with a central scheduler.
# The scheduler is responsible for switching between the small pieces of work that are meant to be executed
# by a single thread.
# The scheduler is also responsible for providing the thread local storage and the global interpreter lock, 
# which is used to  serialize calls to Python C API functions.

# Some Python implementations include an extra layer of abstraction between the interpreter and the CPU. 
# In such implementations, the interpreter does not directly execute the compiled Python code. 
# Instead, it executes an intermediate
