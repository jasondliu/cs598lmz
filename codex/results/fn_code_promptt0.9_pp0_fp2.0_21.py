fn = lambda: None
# Test fn.__code__
self.failIf(fn.__code__ is None)
# Test fn.__annotations__
annotations = fn.__annotations__
self.failUnless(type(annotations) is dict)
# Test fn.__name__
self.failUnlessEqual(fn.__name__, 'lambda')
# Test names
fn = lambda x, : None
self.failUnlessRaises(SyntaxError, compile, 'fn = lambda x, : None', 'f', 'exec')

# more tests for comprehensions
self.failUnless(eval("[x for x in (1, 2)]") == [1, 2])
self.failUnless(eval("[x for x in (1, 2) if x > 1]") == [2])
self.failUnless(eval("[x for x in (1, 2) if x > 1 else 3]") == [2])
# can't use "if" as an expression
try:
    eval("[x for x in (1, 2) if]")
except SyntaxError, e:
    self.failUnless(
        str(e
