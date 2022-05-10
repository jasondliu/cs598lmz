from types import FunctionType
list(FunctionType(f).__code__.co_code)
+[ord('b')]
+[10] # newline
+```

```py
# .co_consts are tuples with the function's constants
f = lambda *a, **b: a

f.__code__.co_consts
# (None, ('a', ('b', 'c')), 'args', 'kwds')
```

```py
# ast.parse(string, mode)
import ast
ast.parse('if 1: print("a")')
# <_ast.Module object at 0x10e463e48>

ast.dump(ast.parse('1 if 1 else 2') )
# "Module(body=[Expr(value=IfExp(test=Num(n=1), body=Num(n=1), orelse=Num(n=2)))]
```

```py
# inspect: is, isinstance, ismethod, isclassm, isdatadescriptor
from inspect import *
import builtins

islambda(lambda: 1) # True

