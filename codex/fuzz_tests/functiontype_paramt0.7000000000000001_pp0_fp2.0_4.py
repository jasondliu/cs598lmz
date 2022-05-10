from types import FunctionType
list(FunctionType(lambda: None, {}).__closure__)

# In python 2.x, the __closure__ is None.
# In python 3.x, the __closure__ is an empty tuple.
# In python 3.x, __closure__ is a tuple that contains cell objects.
# And, a cell object holds an object of local variable.
# In python 3.x, a cell object can be obtained by using the built-in function cell().

# In python 3.x, a cell object can be obtained by using the built-in function cell().
# cell()

# Create a cell object.
cell = cell()
print(str(cell) + " - " + str(type(cell)))
# <cell at 0x0000020D10BD3F48: empty> - <class 'cell'>
# The cell object is empty.

# Create a closure.
def outer(x):
    x += 1
    def inner():
        print(x)
    return inner
f = outer(1)
print(str(f.__closure__) + " - " + str(type(f.__closure__
