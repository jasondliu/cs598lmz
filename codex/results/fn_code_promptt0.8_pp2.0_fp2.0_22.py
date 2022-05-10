fn = lambda: None
# Test fn.__code__.co_varnames
    self.assertEqual(fn.__code__.co_varnames,  ())
    def fn(a,b,c=0,d=1,*e,f,g=2,h=3,**i): pass
    self.assertEqual(fn.__code__.co_varnames,  ('a','b','c','d','f','g','h'))
# Test fn.__code__.co_argcount
    self.assertEqual(fn.__code__.co_argcount,  2)

# Test fn.__code__.co_code
    code_obj = fn.__code__.co_code
    self.assertEqual(type(code_obj),  bytes)
    self.assertEqual(len(code_obj),  1)
    self.assertEqual(code_obj[:1],  b'\x64')

# Test fn.__code__.co_consts
    self.assertEqual(fn.__code__.co_consts,  (None,
