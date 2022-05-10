from types import FunctionType
list(FunctionType(iter([])))

# BlockScope:
def f():
    if 1:
        class C: pass
    else:
        class C: pass
    def g(): return C
    return g()

# WithStatement
with open('filename.txt') as var:
    print(var)

# WithStatement
with open('filename.txt') as var:
    with open('filename2.txt') as var2:
        print(var)
        print(var2)

# WithStatement
with open('filename.txt') as var:
    with open('filename2.txt') as var2:
        print(var)
        print(var2)
    print(var)

# WithStatement
with open('filename.txt'):
    pass

# WithStatement
with open('filename.txt') as var:
    pass
else:
    print('no exception')

# WithStatement
with open('filename.txt') as var:
    pass

# ClassDef
class C:
    x = 10
    def __init__(self):
        self.y =
