from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable

# 但是，如果我们能够获取到函数的__code__属性，就可以直接获得其中的co_varnames，也就是上面提到的参数名列表：

def foo(): pass
foo.__code__.co_varnames
# ('',)

def bar(x): pass
bar.__code__.co_varnames
# ('x',)

def baz(x, y=42): pass
baz.__code__.co_varnames
# ('x', 'y')

def qux(x, *, y): pass
qux.__code__.co_varnames
# ('x', 'y')

def spam(x, y=42
