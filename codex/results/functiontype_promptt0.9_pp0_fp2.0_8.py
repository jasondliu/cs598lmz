import types
# Test types.FunctionType
def foobar(a, b, c, d): pass
field_types = [types.CellType, types.ClassType, types.CodeType,
               types.DictProxyType, types.DictType, types.FrameType,
               types.FunctionType, types.GeneratorType, types.GetSetDescriptorType,
               types.InstanceType, types.LambdaType, types.ListType,
               types.MemberDescriptorType, types.MethodType, types.ModuleType,
               types.TypeType, types.TracebackType]

print 'Testing signature of BuiltinMethodType'
def test_signature(name, spec, expected_defaults):
    try:
        assertEqual(spec.defaults, expected_defaults)
        print '%s: OK' % name
    except:
        print '%s: %r != %r' % (name, spec.defaults, expected_defaults)

from types import BuiltinMethodType

def print_foo_bar():
    print "foo", "bar"

list.foo = print_
