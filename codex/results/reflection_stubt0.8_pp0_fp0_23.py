fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
gi.gi_code = fn
gi.gi_code()

# /usr/local/lib/python3.4/dist-packages/numpy/linalg/linalg.py|_commonType
# http://www.imperva.com/docs/HII_Python_Code_Injection_WP.pdf
# Python allows directives at the beginning of files that affect how the code within the file is interpreted. 
# This can be used to execute code at the beginning of a file before the code within the file executes.

# /usr/local/lib/python3.4/dist-packages/numpy/linalg/linalg.py|_commonType
# https://www.exploit-db.com/exploits/5718/
# The function _commonType() is used to get the type of elements that are common to the input types. 
# The return value of _commonType() will be used in the function evaluate().
# However, due to a bug, _commonType() will accept a string, which will cause the function evaluate() 
# to
