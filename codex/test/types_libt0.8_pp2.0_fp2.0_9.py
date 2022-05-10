import types
types.FunctionType


def bar(b):
    return b


bar(foo)

# x = 1
#
#
# def outer():
#     """
#     x = 0
#     def inner():
#         """
#         x = 1
#         print(x)
#         """
#     inner()
#     print(x)
# """
# outer()
# print(x)


"""
a = 5
def foo():
    b = 6
    print(a, b)
    def bar(a=10, b=20):
        print(a, b)
    bar(10)
    bar(b=1000)
    bar()
foo()
"""


def foo():
    # x = 1
    def bar():
        nonlocal x  # 访问foo 中的x
        y = 2
        x = 1001
        print(x)
    # x = 1
    # y = 2
    x = 1000
    bar()
    print(x)


