from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "addone")(i) for i in range(4))

# line 5:
# <lambda> (x): x + 1
# line 5:
# addone := <function>
# line 6:
# list(addone(0), addone(1), addone(2), addone(3))
# line 6:
# <listcomp> := [0, 1, 2, 3]
# line 6:
# <listcomp>

# --------------------------------------------------

from types import FunctionType
addone = FunctionType(lambda x: x + 1, globals(), "addone")
list(addone(i) for i in range(4))

# line 5:
# <lambda> (x): x + 1
# line 5:
# addone := <function>
# line 6:
# list(addone(0), addone(1), addone(2), addone(3))
# line 6:
# <listcomp> := [0, 1, 2, 3]
# line 6:
# <listcomp>
