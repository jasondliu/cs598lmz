gi = (i for i in ())
# Test gi.gi_code
# type(gi.gi_code)
# print(gi.gi_code.__code__.co_name)
next(gi)
# gi.gi_code
# print(gi.gi_code.__code__.co_name)
next(gi)
# gi.gi_code
# print(gi.gi_code.__code__.co_name)
for i in gi:
    print(i)

def g():
    yield 1

g_o = g()
next(g_o)
# g_o.gi_code
# print(g_o.gi_code.__code__.co_name)
for i in g_o:
    print(i)

#
#
#
#

def f():
    yield

    print(1)
    yield
    yield 1

#

def f():
    print('init f')
    for i in range(3):
        print(i)
        yield i
print("Next f:", next(f()))
print("Next f:", next(
