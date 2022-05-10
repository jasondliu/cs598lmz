import types
# Test types.FunctionType is not overridden by FunctionType in types.py
build_class_unoptimized(types.FunctionType)
# Test types.ClassType is not overridden by ClassType in types.py
build_class_unoptimized(types.ClassType)
# Test types.TypeType is not overridden by TypeType in types.py
build_class_unoptimized(types.TypeType)

def build_class_override(name):
    d = {}
    exec "class %s(object): pass" % name in d
    return d[name]

# Test that override_dict(types) below does not change types.FunctionType
build_class_unoptimized(types.FunctionType)
# Test that override_dict(types) below does not change types.ClassType
build_class_unoptimized(types.ClassType)
# Test that override_dict(types) below does not change types.TypeType
build_class_unoptimized(types.TypeType)

def add_to_dict(dct, key, test):
    dct[key] = build_class_over
