import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score
    def get_score(self):
        return self.score

s = Student('Bob', 'male', 59)
print(type(s.get_score) == types.MethodType)

# Test types.UnboundMethodType
print(type(Student.get_score) == types.UnboundMethodType)

# Test types.BuiltinMethodType
print(type(len) == types.BuiltinMethodType)


