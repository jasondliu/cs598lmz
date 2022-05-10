import types
types.MethodType

def set_age(self,age):
    self.age=age
    print(self)

s.set_age=types.MethodType(set_age,s)
s.set_age(2)
print(s.age)
print(s.sex)
