fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
try:
    sys.getrefcount(fn)
except TypeError:
    pass
else:
    raise AssertionError()
try:
    fn()
except TypeError:
    pass
else:
    raise AssertionError("failed")

__doc__ = '\nscoped_stmt        ::= "global" identifier ("," identifier)*\n                      | "nonlocal" identifier ("," identifier)*\n                      | import_stmt\n                      | "del" target_list\n                      | "pass"\n                      | flow_stmt\n                      | "break"\n                      | "continue"\n                      | "return" [expression_list]\n                      | "raise" [expression ["," expression ["," expression]]]\n                      | "yield" [expression_list]\n                      | stmt_block\n                      | "assert" expression ["," expression]\n                      | assignment_stmt\n                      | expression\n                      | decorator\n'

@staticmethod
def fn():
    def f(a,b=1,
