from types import FunctionType
list(FunctionType(lambda x: x, {}).__closure__)

# Output:
# [<cell at 0x7f8d9c0c7d38: int object at 0x7f8d9c0c7d80>]

# The lambda function has a closure over the integer object.

# The closure is a tuple of cells that contain the bindings for the free variables.
# The cell object is an implementation detail of the CPython interpreter.
# It is not accessible from Python code.
# The cell object has two attributes: cell_contents and ob_ref.
# The cell_contents attribute contains the actual value of the free variable.
# The ob_ref attribute is a reference to the object.
# The ob_ref attribute is used by the garbage collector to track the object.

# The cell object is created when the function is defined.
# The cell_contents attribute is set when the function is called.

# The cell object is created when the function is defined.
# The cell_contents attribute is set when the function is called.

# The cell_contents attribute can be accessed using the cell_cont
