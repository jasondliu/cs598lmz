fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# print(GI_code.co_flags & CO_NESTED)
# print(GI_code.co_flags)
# print(inspect.iscoroutinefunction(fun))
# print(inspect.iscoroutinefunction(fun2))
