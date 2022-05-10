import types
# Test types.FunctionType():
f = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                       argdefs=f.__defaults__,
                       closure=f.__closure__)
f.__closure__
f.__closure__[0].cell_contents


import types
def make_averager():
    count = [0]
    total = [0]

    def averager(new_value):
        count[0] += 1
        total[0] += new_value
        return total[0] / count[0]

    return averager
avg = make_averager()
avg(10)
avg(11)
avg(12)
avg.__code__.co_varnames
avg.__code__.co_freevars
avg.__closure__
avg.__closure__[0].cell_contents
avg.__closure__[1].cell_contents
# Exercise:
def make_averager():
    count = 0
    total = 0

    def
