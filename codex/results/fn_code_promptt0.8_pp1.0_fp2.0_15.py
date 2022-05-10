fn = lambda: None
# Test fn.__code__.co_code == cfn.__code__.co_code is True:
# In [8]: def cfn():
#     ...:     pass
#
# In [9]: fn.__code__.co_code == cfn.__code__.co_code
# Out[9]: True
#
# In [10]: import dis
#
# In [11]: dis.dis(fn)
#  2           0 LOAD_CONST               1 (None)
#              3 RETURN_VALUE


# dis.dis(cfn)

#  2           0 LOAD_CONST               0 (None)
#              3 RETURN_VALUE
