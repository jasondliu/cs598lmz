fn = lambda: None
# Test fn.__code__.co_nlocals
fn.test = lambda: None
test = lambda: None
test.test = lambda: None
# Test fn.__code__.co_stacksize
test2 = lambda: None
test3 = lambda: test2()
test4 = lambda: None
test4.test = lambda: None
test2.__code__.co_stacksize = 5
# Test fn.__code__.co_flags
test5 = lambda: None
test5.__code__.co_flags = 5
# Test fn.__code__.co_code
test6 = lambda: None
test6.__code__.co_code = b'\x00'
# Test fn.__code__.co_consts
test7 = lambda: None
test7.__code__.co_consts = (1,)
# Test fn.__code__.co_names
test8 = lambda: None
test8.__code__.co_names = ('2',)
# Test fn.__code__.co_varnames
test9 = lambda: None
test9.__
