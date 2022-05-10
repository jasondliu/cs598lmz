fn = lambda: None
# Test fn.__code__.co_firstlineno
# PEP 3107: Function Annotations
# check fn.__annotations__
# check fn.__kwdefaults__
#


def ph1(x: "an int", y: "a str" = "hello") -> "result":
    global fn
    fn = ph1
    return "output"

print(ph1(1))
print(ph1.__annotations__)
print(ph1.__annotations__['y'])
print(ph1.__annotations__['x'])


def ph2(y: bool, *x: "an int", **w: "a str"):
    global fn
    fn = ph2
    return "output"

print(ph2(True, 1))
print(ph2.__annotations__)
print(ph2.__annotations__['y'])
print(ph2.__annotations__['x'])
print(ph2.__annotations__['w'])
print(ph2.__kwdefaults__)
#
# expected:
# {'x':
