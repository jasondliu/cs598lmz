gi = (i for i in ())
# Test gi.gi_code is a code object, i.e. gi_code.co_name == '<genexpr>'
test_eq(type(gi.gi_code), types.CodeType)


def regrtest_yield_from(iter_next=iter_next, yield_from=yield_from):
    cnt = 0
    def f():
        nonlocal cnt
        while True:
            cnt += 1
            yield_from(i)
    i = iter_next()
    i.send(None)
    res = f()
    test_eq(cnt, 0)
    test_eq(list(res), [[42, 'spam', (1, 2, 3), 'ham']])
    test_eq(cnt, 4)

def regrtest_yield_from_runtime_exception():
    def f():
        try:
            yield_from(throw_next('spam'))
        except Exception as e:
            yield_from(throw_next('ham'))
            yield sys.exc_info()
            return True
       
