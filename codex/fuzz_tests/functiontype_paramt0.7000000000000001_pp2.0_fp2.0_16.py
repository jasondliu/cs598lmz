from types import FunctionType
list(FunctionType(f.__code__, f.__globals__).__closure__)

# the nonlocal statement
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
avg(10)
avg(11)
avg(12)

# the exec() function
# exec(obj) -> executes the code object obj
exec('print("Hello World")')

# eval() function
# eval(obj) -> evaluates the code object obj
eval('2+2')

# the dir() function
# dir(obj) -> returns a list of the names in the attributes of the object obj
dir([])
dir({})
dir(())
dir('')
dir(int)
dir(float)
dir(complex)

# the help() function
# help(obj) -> shows some help about the obj
help(5)
help(dir)

#
