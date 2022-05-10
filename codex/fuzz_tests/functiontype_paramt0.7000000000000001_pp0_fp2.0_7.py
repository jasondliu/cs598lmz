from types import FunctionType
list(FunctionType(lambda x, y: x+y, {"x": 3, "y": 10}).__code__.co_varnames)

def identity(x=[]):
    x.append(x)
    return x

identity()
identity.__defaults__

identity.__code__.co_consts
identity.__code__.co_freevars
identity.__closure__

# use inspect to get function arguments
import inspect
print(inspect.signature(identity))


# **Function Annotations**
def add(x: int, y: int) -> int:
    return x + y

print(add.__annotations__)
inspect.signature(add)
inspect.signature(add).return_annotation
