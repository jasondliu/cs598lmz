from types import FunctionType
list(FunctionType(x,globals())() for x in [
  'def f(x): return x*x',
  'def f(x): return x+x',
  'def f(x): return x**2',
  'def f(x): return x*2',
  'def f(x): return x**3',
  'def f(x): return x+1',
  'def f(x): return x+2',
  'def f(x): return x**4',
  'def f(x): return x*3',
  'def f(x): return x+3',
])
</code>

