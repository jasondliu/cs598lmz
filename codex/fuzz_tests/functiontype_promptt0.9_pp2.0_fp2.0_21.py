import types
# Test types.FunctionType
class A(types.FunctionType):
  pass

# Test types.LambdaType
def A(x):
  return lambda x:x
# Test types.GeneratorType
# Test types.TracebackType
try:
  raise Exception()
except:
  a = sys.exc_info()[2]
# Test types.FrameType
import inspect
def A():
  return inspect.currentframe()
# Test types.GetSetDescriptorType
class A(object):
  @property
  def A(self):
    pass
# Test types.MemberDescriptorType
# Test types.DictProxyType
import abc
A = abc.ABCMeta('A', (), {})
# Test types.NotImplementedType
A = NotImplemented
# Test types.EllipsisType
A = ...
