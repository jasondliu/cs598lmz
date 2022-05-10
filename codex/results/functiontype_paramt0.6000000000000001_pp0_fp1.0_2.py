from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo').__closure__)

# test code
from types import FunctionType
def make_adder(augend):
    def add(addend):
        return augend + addend
    return add

add_three = make_adder(3)
add_four = make_adder(4)
print(add_three(1))
print(add_four(1))
print(FunctionType(lambda x: x, globals(), 'foo').__closure__)
