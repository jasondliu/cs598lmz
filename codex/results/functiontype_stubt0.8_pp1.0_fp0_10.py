from types import FunctionType
a = (x for x in [1])

@type_check(int, int)
def add(a, b):
    return a + b

print(add(22, 1))
#print(add("12", 1))
