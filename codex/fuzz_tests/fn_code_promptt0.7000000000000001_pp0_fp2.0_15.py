fn = lambda: None
# Test fn.__code__.co_varnames
def fn_test(arg, **kwargs):
    pass
test(fn_test.__code__.co_varnames == ('arg', 'kwargs'))
# Test fn.__code__.co_argcount
test(fn_test.__code__.co_argcount == 1)
# Test fn.__code__.co_kwonlyargcount
test(fn_test.__code__.co_kwonlyargcount == 1)
# Test fn.__code__.co_nlocals
test(fn_test.__code__.co_nlocals == 2)
# Test fn.__code__.co_posonlyargcount
test(fn_test.__code__.co_posonlyargcount == 0)
# Test __annotations__
def fn_test(arg: str, arg2: int = 2, *args: tuple, kwarg: bool, **kwargs: dict):
    pass
test(fn_test.__annotations__['arg'] == str)
# Test fn.__code__.co_consts

