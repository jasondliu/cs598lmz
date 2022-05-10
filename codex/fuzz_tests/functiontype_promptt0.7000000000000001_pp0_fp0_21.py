import types
# Test types.FunctionType
assert isinstance(Predictor.get_predictor, types.FunctionType)
assert isinstance(Predictor.get_predictor_instance_method, types.MethodType)
assert isinstance(Predictor.get_predictor_instance_method_raw, types.FunctionType)
assert isinstance(Predictor.get_predictor_class_method, types.MethodType)
assert isinstance(Predictor.get_predictor_class_method_raw, types.FunctionType)
assert isinstance(Predictor.get_predictor_static_method, types.FunctionType)
assert isinstance(Predictor.get_predictor_static_method_raw, types.FunctionType)

# Test types.LambdaType
# Test types.GeneratorType

# Test types.CodeType

# Test types.TypeType
assert isinstance(Predictor, types.TypeType)

# Test types.UnboundMethodType
# Test types.ModuleType
# Test types.FileType
# Test types.BuiltinFunctionType
# Test types
