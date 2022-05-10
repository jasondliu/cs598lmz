fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_firstlineno
"""

var = "abcde"

def foo():
    x = 'def'
    for i in range(10):
        if i % 2 == 0:
            exec("y = 'even'")
        else:
            exec("y = 'odd'")
        print(x)
        print(y)
        print(var)

foo()

def bar():
    x = 'def'
    for i in range(10):
        if i % 2 == 0:
            y = 'even'
        else:
            y = 'odd'
        print(x)
        print(y)
        print(var)

bar()
