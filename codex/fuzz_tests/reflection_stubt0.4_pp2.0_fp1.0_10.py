fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# should not crash

# check that the exception is the expected one
# and that the traceback is properly set

import sys

try:
    fn()
except TypeError as e:
    if str(e) != "unsupported operand type(s) for +: 'code' and 'generator'":
        print("FAIL: wrong exception raised:", e)
    else:
        tb = sys.exc_info()[2]
        if tb.tb_next is None:
            print("FAIL: no traceback")
        else:
            if tb.tb_next.tb_lineno != 12:
                print("FAIL: wrong line number in traceback:", tb.tb_next.tb_lineno)
            else:
                print("OK")
