from types import FunctionType
list(FunctionType(expr.code, expr.__globals__)(*expr.args))

$ python2 -c """
import array 
x = lambda: 'foo'
y = lambda: array.array('b', [ord(c) for c in x()])
z = lambda: [c for c in y()]
import dis
expr = dis.findlinestarts(z.__code__)[0][2].next
print '%s(%s)' % (expr.__name__, ', '.join(expr.__globals__[n] for n in expr.co_names))
import types
list(types.FunctionType(expr.func_code, expr.__globals__, expr.__name__, expr.func_defaults, expr.func_closure)())
"""

def array(typecode, initializer):
    return array(typecode, initializer)
list(array('b', 'foo'))
</code>

