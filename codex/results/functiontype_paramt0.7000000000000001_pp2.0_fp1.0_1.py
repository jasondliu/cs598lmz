from types import FunctionType
list(FunctionType('foo', '').__globals__.keys())

"""
['__builtins__', '__name__', '__doc__', '__package__']
"""

import math
list(math.__dict__.keys())

"""
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'pi', 'e', 'tau', 'inf', 'nan', '__docformat__', '__all__', '__version__', '__file__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ld
