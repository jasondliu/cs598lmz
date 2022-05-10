from types import FunctionType
a = (x for x in [1])
print(type(a))

for i in a:
    print(i)

l = [x for x in a]
print(l)

print(list(a))

import dis
func = """
def f(x):
    return x
"""
# exec(func)
dis.dis(func)
