from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code object
import dis
dis.dis(lambda x: x)

# bytecode
def compile_lambda(source):
    return compile(source, '<string>', 'eval')

def make_lambda_function(source, globs, locs=None):
    return eval(compile_lambda(source), globs, locs)

make_lambda_function('x, y: x + y', {})

# function object
import types
def make_function(source, globs=None, locs=None):
    return types.FunctionType(compile(source, '<string>', 'exec'), globs, 'f', None, locs)

make_function('def f(x, y): return x + y')

# function object
import types
def make_function(code, globs=None, locs=None):
    return types.FunctionType(code, globs, 'f', None, locs)

make_function(compile('def f(x, y): return x +
