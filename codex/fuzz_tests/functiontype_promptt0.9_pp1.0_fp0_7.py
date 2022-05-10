import types
# Test types.FunctionType
def function_func(x):
    return x

local_vars = list(filter(lambda x: isinstance(locals()[x], types.FunctionType), locals()))
# local_vars = [[k, v] for k, v in locals().items() if isinstance(v, types.FunctionType)]
print(local_vars)

# Test types.LambdaType
# lambda_func = lambda x: x

# local_vars = filter(lambda x: isinstance(locals()[x], types.LambdaType), locals())
# print(local_vars)

# Test types.ClassType
class ClassTypeClass:

    @classmethod
    def a_class_method():
        pass
    
    def an_instance_method(self):
        pass

local_vars = list(filter(lambda x: isinstance(locals()[x], types.ClassType), locals()))
print(local_vars)

# Test types.InstanceType
instance_obj = ClassTypeClass()

local_vars = list(
