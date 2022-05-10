import types
types.MethodType(print, None)
# <function print>

f = lambda x: x + 1
f(2)
# 3

g = lambda x: lambda y: x + y
g(1)(2)
# 3

class Foo:
    bar = "baz"

foo = Foo()

if foo.bar == "baz":
    print("baz")
# baz

if hasattr(foo, "bar"):
    print("bar")
# bar

setattr(foo, "bar", 5)
if foo.bar == 5:
    print("5")
# 5

delattr(foo, "bar")
if not hasattr(foo, "bar"):
    print("bar")
# bar

# C style comments are invalid in Python

# Pythonic code is
names = [ "Alice", "Bob", "Charlie", "Daina", "Elvis" ]
