fn = lambda: None
# Test fn.__code__ and fn.__globals__
# >>> fn.__code__
# <code object <lambda> at 0x7f9b7a1f4770, file "<stdin>", line 1>
# >>> fn.__code__.co_code
# b'|\x00|\x01\x17\x00S\x00'
# >>> fn.__code__.co_filename
# '<stdin>'
# >>> fn.__code__.co_name
# '<lambda>' # not fn.__name__ because we are using lambda
# >>> fn.__globals__ == globals()
# True

# In Python 3, we can also use lambda: None to replace the function.
# NOTE: the following is for Python 3!
# >>> (lambda: None).__code__
# <code object <lambda> at 0x7ff5a3d0c410, file "<stdin>", line 1>
# >>> (lambda: None).__code__.co_code
# b'|\x00\x83\x01\x00d\
