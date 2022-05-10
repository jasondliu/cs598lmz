fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

# TypeError: 'generator' object is not callable

# fn.__code__ = 'hello'
# try:
#     fn()
# except TypeError as e:
#     print(e)

# TypeError: 'str' object is not callable

# fn.__code__ = 1
# try:
#     fn()
# except TypeError as e:
#     print(e)

# TypeError: 'int' object is not callable

# fn.__code__ = object()
# try:
#     fn()
# except TypeError as e:
#     print(e)

# TypeError: 'object' object is not callable

# fn.__code__ = type
# try:
#     fn()
# except TypeError as e:
#     print(e)

# TypeError: 'type' object is not callable

# fn.__code__ = type(fn)
# try:
#     fn()

