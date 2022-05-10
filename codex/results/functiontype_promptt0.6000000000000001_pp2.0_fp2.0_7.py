import types
# Test types.FunctionType
# This is easy to check and is a good early test.
assert type(type) is types.BuiltinFunctionType
# Test types.BuiltinFunctionType
assert type(id) is types.BuiltinFunctionType
# Test types.MethodType
assert type(list.append) is types.MethodType
# Test types.UnboundMethodType
assert type(list.append) is types.MethodType
assert type(list.append) is types.MethodType
# Test types.ModuleType
assert type(types) is types.ModuleType

# Test sys.flags
import sys
assert isinstance(sys.flags, types.SimpleNamespace)
assert sys.flags.debug is False
assert sys.flags.py3k_warning is False
assert sys.flags.division_warning is False
assert sys.flags.division_new is False
assert sys.flags.inspect is False
assert sys.flags.interactive is False
assert sys.flags.optimize is 0
assert sys.flags.dont_write_bytecode is False
assert sys.flags.no_user_site is False
assert sys.flags.
