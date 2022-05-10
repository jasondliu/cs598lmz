fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TODO:
# bug https://bugs.python.org/issue35647
# def f():
#     print(1)
#     yield 1
#     print(2)
#
# f.__code__ = f
# f()
#
#
# def f():
#     print(1)
#     yield 1
#     print(2)
#
#
# f.__code__ = f.__code__.__code__
# f()
