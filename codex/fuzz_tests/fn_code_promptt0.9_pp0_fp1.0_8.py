fn = lambda: None
# Test fn.__code__.co_filename
testfn.__code__.__dict__['co_filename'] = 'h:\xdir\has\special\chars'
testfn.__code__.__dict__['co_firstlineno'] = 1
run_test(testfn, '<function %s from h:\\xdir\\has\\special\\chars:1>' % testfn.__code__.co_name)

# Test a failure to get the filename
testfn.__code__.__dict__['co_filename'] = None
run_test(testfn, '<function %s>' % testfn.__code__.co_name)

# Test fn.__code__.co_firstlineno
for lineno in (-5, 0, 3):
    testfn.__code__.__dict__['co_firstlineno'] = lineno
    run_test(testfn, '<function %s from h:\\xdir\\has\\special\\chars:%s>' % (testfn.__code__.co_name, lineno or None))

# Test fn
