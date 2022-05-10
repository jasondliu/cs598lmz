fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError as e:
    print(e)

# TypeError: 'generator' object is not callable

# fn.__code__ = 42
#
# try:
#     fn()
# except TypeError as e:
#     print(e)
#
# # TypeError: 'int' object is not callable
#
# fn.__code__ = (i for i in ())
#
# try:
#     fn()
# except TypeError as e:
#     print(e)
#
# # TypeError: 'generator' object is not callable
#
# fn.__code__ = [1, 2, 3]
#
# try:
#     fn()
# except TypeError as e:
#     print(e)
#
# # TypeError: 'list' object is not callable
#
# fn.__code__ = 'abc'
#
# try:
#     fn()
# except TypeError as e:
#     print(e)
#
# # TypeError:
