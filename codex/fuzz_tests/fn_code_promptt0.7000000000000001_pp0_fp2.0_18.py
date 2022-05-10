fn = lambda: None
# Test fn.__code__.co_filename.startswith(sys.prefix)
# Test fn.__code__.co_filename.startswith(os.path.join(sys.prefix, 'python', 'Lib'))
# Test fn.__code__.co_filename.startswith(os.path.join(sys.prefix, 'Lib'))
# Test fn.__code__.co_filename.startswith(os.path.join(sys.prefix, 'lib-dynload'))

# Test that __builtins__ is the same as sys.modules['__builtins__'].
if __builtins__ is not sys.modules['__builtins__']:
    raise TestFailed(
        "__builtins__ is not the same object as sys.modules['__builtins__'].")

# make sure that sys.modules[__name__] is this very module
if sys.modules[__name__] is not sys.modules['test.test_sys']:
    raise TestFailed(
        "sys.modules[__name__] is not the same object as sys.modules['test.
