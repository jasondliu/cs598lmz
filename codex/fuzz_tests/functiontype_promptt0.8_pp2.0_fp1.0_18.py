import types
# Test types.FunctionType
# function type
def f(): pass
function_type_var = f
print(type(function_type_var))
print(type(f) == types.FunctionType)
# lambda function
lambda_function_var = lambda x: x
print(type(lambda_function_var))
# method type
class MethodType(object):
    def __init__(self):
        self.x = 9
    def sum(self, a):
        return self.x + a
method_type_var = MethodType().sum
print(type(method_type_var))

# Test types.GeneratorType
# generator type
generator_type_var = (x for x in "abcd")
print(type(generator_type_var))

# Test types.GetSetDescriptorType
class GetSetDescriptorType(object):
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
# Test types.MemberDescriptorType
# Test types.Lamb
