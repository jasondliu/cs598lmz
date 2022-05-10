from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f').__closure__)

# __closure__ is a tuple of cells, and a cell is a container for a reference to an object
# a cell is created when a function is defined and it is used to store the value of a free variable
# the cell object is the only way to access the contents of a closure
# a cell is not a container for a value, it is a container for a reference to a value
# a cell can be accessed via its cell_contents attribute

# the following code demonstrates how a cell is created when a function is defined

def f1(a):
    def g(b):
        return a + b
    return g

f1(1)(2)

# g is a function that has a free variable a
# when g is defined, a cell is created to store the reference to a
# when f1 is called, g is returned, and the cell is part of g's closure
# the cell is part of g's __closure__ attribute, which is a tuple of cells
# the cell can be accessed via the cell_contents attribute

# the
