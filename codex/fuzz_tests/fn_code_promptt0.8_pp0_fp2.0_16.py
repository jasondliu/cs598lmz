fn = lambda: None
# Test fn.__code__, fn.__name__
self.assertEqual(fn.__code__.co_filename, "&lt;string&gt;"
self.assertEqual(fn.__code__.co_name, "&lt;lambda&gt;")
</code>

