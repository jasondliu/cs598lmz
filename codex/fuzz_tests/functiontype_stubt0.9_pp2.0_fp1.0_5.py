from types import FunctionType
a = (x for x in [1])
b = (x for x in range(0))

# @benchmark
for n in range(10000000):
    # print(n)
    # pass
    a.__iter__()
    b.__iter__()
    # c.__iter__()


# @benchmark
# def func():
#     for n in range(10000000):
#         a.__iter__()
#         b.__iter__()
#         c.__iter__()
#
# func()


class A:
    def __init__(self):
        self.__dict__['key'] = 'value'

    def __getattr__(self, item):
        if item == 'key':
            return 'value2'


a = A()
print(dir(a))
print(a.key)

a = (x for x in [1])
print(a.__getattribute__('gi_frame'))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a
