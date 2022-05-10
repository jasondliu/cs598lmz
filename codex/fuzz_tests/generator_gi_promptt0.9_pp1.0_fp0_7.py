gi = (i for i in ())
# Test gi.gi_code == None, which means that it's a generator-iterator
self.assertEqual(gi.gi_frame.f_code, None)

# Python function
def simple(arg):
    return arg

sf = simple(4)
# Test f.f_code which should be a code object
self.assertEqual(sf.f_code.co_name, 'simple')

self.assertEqual(simple.__closure__, None)
self.assertEqual(simple.__annotations__, {})

# Test comparison operations of FrameInfo and CodeInfo
self.assertEqual(cf > ff, True)
self.assertEqual(cf < gi, True)
self.assertEqual(cf == cf, True)
self.assertEqual(cf != ff, True)

# Test ModuleInfo
mi = inspect.getmoduleinfo(inspect.__file__)
self.assertEqual(tuple(sorted(mi)),
                 ('file', 'name', 'package', 'version'))
self.assertTrue(mi.name.endswith('inspect'))
