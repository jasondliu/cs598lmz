from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), "square")(3))

list(map(FunctionType(lambda x: x**2, globals(), "square"), [1, 2, 3]))

list(map(lambda x: x**2, [1, 2, 3]))
#%%

def make_adder(augend):
    def adder(addend):
        return augend + addend
    return adder

add_ten = make_adder(10)
add_ten(3)

def make_adder(augend):
    return lambda addend: augend + addend

add_ten = make_adder(10)
add_ten(3)

#%%

def make_adder(augend):
    return lambda addend: augend + addend

def make_incrementor(base):
    return make_adder(base)

increment_by_ten = make_incrementor(10)
increment_by_ten(3)

def make_incrementor(base):
    return make_adder(base)
