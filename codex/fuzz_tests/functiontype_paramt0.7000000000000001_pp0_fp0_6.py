from types import FunctionType
list(FunctionType(lambda: None, {}, None, None, None).__code__.co_code)
 
# >>> list(FunctionType(lambda: None, {}, None, None, None).__code__.co_code)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'code' object is not iterable
