fn = lambda: None
gi = (i for i in ())
fn.__code__ = code
gi.gi_code = code

# This is a bit of a hack, but it lets us get the line number easily
code.co_firstlineno = inspect.currentframe().f_lineno + 1

import dis
dis.dis(code)

# The disassembled output should look something like this:
# 1           0 LOAD_CONST               0 (0)
#             2 LOAD_CONST               1 (None)
#             4 IMPORT_NAME              0 (sys)
#             6 STORE_NAME               0 (sys)
#
# 2           8 LOAD_NAME                0 (sys)
#            10 LOAD_ATTR                1 (stdout)
#            12 LOAD_ATTR                2 (write)
#            14 LOAD_CONST               2 ('Hello World!\n')
#            16 CALL_FUNCTION            1
#            18 POP_TOP
#            20 LOAD_CONST               1 (None)
#            22 RETURN_VALUE

# The first two lines are a special case, since they're the function
# definition.  The next
