from types import FunctionType
a = (x for x in [1])
a[0]

import inspect

s = '''
def f(x):
	return x + 5
'''
ff = [fn for fn, code in globals().items() if isinstance(code, FunctionType)]
fns = [fn for fn, code in globals().items() if isinstance(code, FunctionType) and inspect.getsourcefile(code) == inspect.getfile(inspect.currentframe())]

fns

def f(x):
	return x + 5

inspect.getsource(f)
inspect.getsource(inspect.getmodule(f))

s = inspect.getsource(f)
ff = {}
exec s in ff
ff

def f(x):
	return x + 5

def g(x):
	return f(x)

inspect.getsource(g)
inspect.getsource(inspect.getmodule(g))

inspect.getsource(lambda x: x + 5)

s = '''
def f(x):
	def g(x):
		return
