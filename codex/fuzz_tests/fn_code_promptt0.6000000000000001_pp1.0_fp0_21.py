fn = lambda: None
# Test fn.__code__
self.assertEqual(fn.__code__.co_argcount, 0)
self.assertEqual(fn.__code__.co_filename, __file__) # compiled from
self.assertEqual(fn.__code__.co_name, '<lambda>')
self.assertIn(fn.__code__.co_name, repr(fn.__code__))
self.assertIn(fn.__code__.co_filename, repr(fn.__code__))
self.assertEqual(fn.__code__.co_varnames, ())
# Test fn.__defaults__
self.assertEqual(fn.__defaults__, None)
# Test fn.__closure__
self.assertEqual(fn.__closure__, None)
# Test fn.__globals__
self.assertEqual(fn.__globals__, globals())

fn = lambda x: None
# Test fn.__code__
self.assertEqual(fn.__code__.co_argcount, 1)
self.assertEqual(fn.
