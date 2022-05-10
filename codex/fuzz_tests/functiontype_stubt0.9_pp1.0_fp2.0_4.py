from types import FunctionType
a = (x for x in [1])
a

def a():
    return 0

print type(a) == FunctionType

from ast import AST, Name, Load, Call
from ast import FunctionDef, Return, BinOp, Add, Store
from ast import parse

body = [
    Return(BinOp(Name('a', Load()), Add(), Name('b', Load())))
]

args = [
    Name('a', Load()),
    Name('b', Load())
]

def2 = FunctionDef('f', args, body)

print type(def2)

tree = parse('f(a, b)')

print tree
print type(tree)
print tree._fields
print type(tree.body)
print tree.body[0]
print tree.body[0]._fields
print type(tree.body[0].value)

tree.body[0].value = def2

print tree
