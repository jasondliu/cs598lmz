fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
"""

code = compile(code, '<stdin>', 'exec')

import dis
dis.dis(code)

# Disassembly of <code object <module> at 0x7f3b3f41c810, file "<stdin>", line 1>:
#   1           0 LOAD_CONST               0 (<code object <lambda> at 0x7f3b3f41c8d0, file "<stdin>", line 1>)
#               2 LOAD_CONST               1 ('<lambda>')
#               4 MAKE_FUNCTION            0
#               6 STORE_NAME               0 (fn)
#
#   2           8 LOAD_NAME                1 (i)
#              10 LOAD_CONST               2 (1)
#              12 BUILD_TUPLE              1
#              14 GET_ITER
#              16 CALL_FUNCTION            1
#              18 STORE_NAME               2 (gi)
#
#   3          20 LOAD_NAME                0 (fn)
#              22 LOAD_ATTR               
