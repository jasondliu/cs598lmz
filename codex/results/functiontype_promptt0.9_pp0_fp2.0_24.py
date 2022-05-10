import types
# Test types.FunctionType
def to_upper(s: str) -> str:
    return s.upper()
assert(hasattr(to_upper, '__annotations__'))
assert(isinstance(to_upper, types.FunctionType))
assert(isinstance(to_upper, types.BuiltinFunctionType) is False)
assert(isinstance(len, types.BuiltinFunctionType))
assert(isinstance(max, types.BuiltinFunctionType))
assert(isinstance(min, types.BuiltinFunctionType))
# Test types.ModuleType
import types
assert(isinstance(types, types.ModuleType))
assert(types.__package__ == 'types')
assert(types.__name__ == 'types')
assert(types.__file__)
assert(str.__module__ == 'builtins')
# Test types.FrameType
def main(): pass
assert(isinstance(types.getouterframes(types.getouterframes(types.currentframe())[0][0])[0][0], types.FrameType))
assert(isinstance(types.getouterframes(types.getouterframes(types
