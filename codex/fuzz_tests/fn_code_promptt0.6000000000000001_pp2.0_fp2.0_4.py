fn = lambda: None
# Test fn.__code__
self.assertEqual(fn.__code__.co_argcount, 0)
self.assertEqual(fn.__code__.co_nlocals, 0)
self.assertEqual(fn.__code__.co_stacksize, 2)
self.assertEqual(fn.__code__.co_flags, 67)
# Test fn.__defaults__
self.assertEqual(fn.__defaults__, None)
# Test fn.__closure__
self.assertEqual(fn.__closure__, None)
# Test fn.__globals__
self.assertEqual(fn.__globals__['__name__'], __name__)
# Test fn.__dict__
self.assertEqual(fn.__dict__, {})
# Test fn.__doc__
self.assertEqual(fn.__doc__, None)
# Test fn.__name__
self.assertEqual(fn.__name__, '<lambda>')
# Test fn.__module__
self.assertEqual(fn.__module__
