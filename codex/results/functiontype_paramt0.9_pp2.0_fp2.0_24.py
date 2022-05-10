from types import FunctionType
list(FunctionType(g, {}, 'x'))
# Out[6]: ['a', '1', '_', 'ع']
 
</code>
But the non-letters are just ords, such as <code>ord('1') == 49</code>.

<code>len(g.co_code)
</code>
You can find the length of codes (Section 2).

<code>import dis
dis.dis(g)
# Out[8]: 
# 0           0 LOAD_CONST               1 (0)
#             2 STORE_FAST               0 (a)
# 
# 1           4 LOAD_CONST               2 (1)
#             6 SETUP_LOOP              56 (to 66)
#             8 LOAD_FAST                0 (a)
#            10 LOAD_CONST               2 (1)
#            12 BINARY_ADD
#            14 STORE_FAST               0 (a)
#            16 LOAD_FAST                0 (a)
#            18 LOAD_CONST               3 (4)
#            20 COMPARE_
