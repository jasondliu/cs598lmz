fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', 'test')
# Test fn.__code__.co_code
setattr(fn.__code__,'co_code','test')
print([i for i in test(fn)])

test(1)

test(1,2,3)

test([])

test([1,2,3])
