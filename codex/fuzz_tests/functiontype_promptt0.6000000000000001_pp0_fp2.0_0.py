import types
# Test types.FunctionType
def f(): pass
def f_gen(): yield
def f_gen_2(): yield 1; yield 2
def f_gen_3():
    yield 1
    yield 2
def f_gen_4():
    yield
    yield
def f_gen_5(): yield 1; yield 2; yield 3
def f_gen_6():
    yield 1
    yield 2
    yield 3
def f_gen_7():
    yield from x
    yield from y
def f_gen_8():
    yield from x
def f_gen_9():
    yield from x
    yield
def f_gen_10():
    yield
    yield from x
def f_gen_11():
    yield
    yield from x
    yield
def f_gen_12():
    yield from x
    yield
    yield from y
def f_gen_13():
    yield from x
    yield
    yield from y
    yield
def f_gen_14():
    yield
    yield from x
    yield
    yield from y
def f_gen_15():
    yield
   
