fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# def foo():
#     return 1
#
#
# fn = lambda :None
# print(fn.__code__)
# fn.__code__ = foo.__code__
# print(fn.__code__)
# print(fn())
