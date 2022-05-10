from types import FunctionType
list(FunctionType())

class function(object):
    
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        return list(self.func)

print(function(list))

def f(a, b, c=[]):
    c.append(1)
    c.append(2)
    c.append(3)
    return a + b

f.func_code
print(f(2, 3))
print(f(2, 3))
print(f(2, 3))
