fn = lambda: None
# Test fn.__code__
# CHECK: AttributeTest.py:7: fn.<lambda>.__code__ = <code object <lambda>
print("fn.__code__ = {!r}".format(fn.__code__))
# Test fn.__code__.co_name
# CHECK-NEXT: {.co_name.__get__ = <built-in method __get__ of code object>}
# CHECK-NEXT: fn.__code__.co_name = <method-wrapper object at 0x{{.*}}>
print("fn.__code__.co_name = {!r}".format(fn.__code__.co_name))
# Test dir(code)
# CHECK: {
# CHECK-NEXT: .__class__ = <class 'code'>
# CHECK-NEXT: .__module__ = code
# CHECK-NEXT: .__name__ = code
# CHECK-NEXT: .co_argcount = 0
# CHECK-NEXT: .co_cellvars = 
# CHECK-NEXT: .co_code =
