from types import FunctionType
list(FunctionType(f1, globals(), 'f1') for f1 in (lambda x, y: (x+y, x-y),
  lambda x, y: (x*y, x/y) if y else (x**2, x**0.5))) """
function: [['x', 'y'], [['return', ['tuple', [['+', 'x', 'y'], ['-', 'x', 'y']]]]], 'f1']
function: [['x', 'y'], [['if', 'y', ['else', [['return', ['tuple', [['*', 'x', 'y'], ['/', 'x', 'y']]]], [['return', ['tuple', [['**', 'x', 'y'], ['**', 'x', 'y']]]]]]]]], 'f1']"""

import dis

def b(f):
    return [dis.Bytecode(f)]

def t(s):
    return list(dis.Bytecode(s.encode('utf-8')))

f = "lambda x, y:
