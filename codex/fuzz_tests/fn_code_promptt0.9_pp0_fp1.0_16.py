fn = lambda: None
# Test fn.__code__
"""
<48>           0 LOAD_GLOBAL              0 (None)
            3 RETURN_VALUE
"""
#print(fn.__code__.co_code)
#print(fn.__code__.co_code[:])

print(dis.dis(fn))
"""
  2           0 LOAD_CONST               1 (<code object <lambda> at 0x7fd6f67ef8b0, file "test.py", line 2>)
              3 LOAD_CONST               2 ('<lambda>')
              6 MAKE_FUNCTION            0
              9 STORE_NAME               0 (fn)

  3          12 LOAD_CONST               0 (0)
             15 LOAD_CONST               3 (None)
             18 RETURN_VALUE
"""
print(fn.__code__.co_code[:])
"""
b'|\x00|\x01\x17\x00}\x03h\x01\x02\x00d\x00}\x01|\x00|\x01d\x01\x17\x
