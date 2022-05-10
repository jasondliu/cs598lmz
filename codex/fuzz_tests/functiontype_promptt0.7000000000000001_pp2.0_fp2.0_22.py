import types
# Test types.FunctionType()
for name, obj in types.__dict__.items():
    if isinstance(obj, types.FunctionType):
        print(name)

# Test types.ClassType()
def test_instance(obj):
    if isinstance(obj, types.ClassType):
        print(obj)
test_instance(test_instance)

# Test types.InstanceType()
def test_instance(obj):
    if isinstance(obj, types.InstanceType):
        print(obj)
test_instance(test_instance)

# Test types.MethodType()
def test_instance(obj):
    if isinstance(obj, types.MethodType):
        print(obj)
test_instance(test_instance)

# Test types.ModuleType()
for name, obj in types.__dict__.items():
    if isinstance(obj, types.ModuleType):
        print(name)

# Test types.UnboundMethodType()
def test_instance(obj):
    if isinstance(obj, types.UnboundMethodType):
        print(obj)
test_instance
