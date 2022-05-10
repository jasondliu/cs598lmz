gi = (i for i in ())
# Test gi.gi_code
# >>> gi.gi_code is None
# True
# >>> gi.gi_frame is None
# True
# >>> gi.gi_running
# False
# >>> gi.gi_yieldfrom is None
# True
# >>> gi.gi_frame is None
# True

# gi.__name__ = 'my_gen'
# gi.__qualname__ = 'my_gen'
# gi.__qualname__ = 'my_gen'
# gi.
# gi.gi_frame.
# gi.gi_frame.f_back.
# gi.gi_frame.f_back.f_code.

# Using a function as a decorator
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(
#             original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# # class decorator_class(object):
# #
