from types import FunctionType
list(FunctionType(f.bytecode, f.func_globals))

# Example 4-3. Using func_closure to access the attributes bound to free variables
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

avg = make_averager()
print avg.__code__.co_freevars  # ('count', 'total')
print avg.__closure__  # (<cell at 0x1004e4d08: int object at 0x100287190>, <cell at 0x1004e4d40: int object at 0x100287190>)
print avg.__closure__[0].cell_contents  # 1
print avg.__closure__[1].cell_contents  # 1

# Example 4-4. Using func_closure and func_code to clone a function
from types import FunctionType
def make_averager():
    count = 0
    total = 0

    def averager(
