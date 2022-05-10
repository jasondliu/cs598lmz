import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is no longer true in Python 3
# >>> syntax error (missing colon)
# >>> if x=0:
#            print(x)
#                     



# >>> x=3
# >>> y=x
# >>> x=x+2
# >>> print(x)
# 5
# >>> print(y)
# 3
# >>> 

# >>> x=3
# >>> y=x
# >>> x+=2
# >>> print(x)
# 5
# >>> print(y)
# 3
# >>> 

# >>> x=3
# >>> y=x
# >>> x-=1
# >>> print(x)
# 2
# >>> print(y)
# 3
# >>> 

# >>> x=3
# >>> y=x
# >>> x*=2
# >>> print(x)
# 6
# >>> print(y)
# 3
# >>> 

# >>> x=3
# >>> y=x
# >>> x/=2
# >>> print(x)
# 1
