fn = lambda: None
# Test fn.__code__, fn.__globals__, fn.__closure__, fn.__name__, fn.__module__
# Test fn.__defaults__, fn.__kwdefaults__
# Test fn.__annotations__

# Method descriptors
test_fn = lambda a: None
test_fn.__code__
test_fn.__self__
# Test test_fn.__func__ which is equal to test_fn

# Static methods
class A:
  def sm1(a):
    pass
  sm2 = staticmethod(sm1)
  @staticmethod
  def sm3():
    pass
A.sm1.__func__
A.sm1.__self__ # Equals to A
# Test A.sm2.__func__, A.sm2.__self__
A.sm3.__func__
A.sm3.__self__ # Equals to A

# Class methods
class B:
  def cm1(cls, a):
    pass
  cm2 = classmethod(cm1)
  @classmethod
  def cm3
