fn = lambda: None
# Test fn.__code__.co_argcount (issue13961)
setattr(fn, '__code__', 42 ** 42)

# Test file methods (issue12910)
with open(__file__) as f:
    f.read(1)
    f.seek(0)
    f.write('test')

print('test_builtins: OK')
