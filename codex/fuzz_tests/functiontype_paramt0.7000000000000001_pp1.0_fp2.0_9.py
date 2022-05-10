from types import FunctionType
list(FunctionType(vars(f)[ '__code__' ], globals()).__closure__)

#('x', 1)

#The contents of __closure__ are tuples containing references to
# to the cell variables used by the closure. To access the values
# of these variables, extract the cell object from the tuple, and
# use its cell_contents property.

from types import FunctionType
c = list(FunctionType(vars(f)[ '__code__' ], globals()).__closure__)[ 0 ]
c.cell_contents

#1

#It's possible to change the contents of a cell.

from types import FunctionType
c = list(FunctionType(vars(f)[ '__code__' ], globals()).__closure__)[ 0 ]
c.cell_contents = 2
f()

#2

#As you can see, high-level functions are quite complex, and
# are actually implemented as a lot of low-level objects.
# When you call a function, the interpreter has to look up
# the function definition (e.g. via a global symbol table
