from types import FunctionType
list(FunctionType(my_func.__code__, globals(), 'my_func', my_func.__defaults__))

# my_func.__code__.co_argcount   # 2
# my_func.__code__.co_kwonlyargcount   # 0
# my_func.__code__.co_nlocals   # 3
# my_func.__code__.co_stacksize   # 2
# my_func.__code__.co_flags   # 67
# my_func.__code__.co_code   # b'd\x00\x00|\x00\x00|\x01\x00|\x00\x00\x17\x00\x00S'
# my_func.__code__.co_consts   # (None,)
# my_func.__code__.co_names   # ('math', 'sqrt')
# my_func.__code__.co_varnames   # ('x', 'y', 'z')
# my_func.__code__.co_freevars   # ()

