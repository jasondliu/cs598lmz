import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '<Person: %s(%s)>' % (self.name, self.age)
#
#     __repr__ = __str__
#
#
# p = Person('Michael', 30)
# print(p)

# class Student(Person):
#     def __init__(self, name, age, score):
#         super().__init__(name, age)
#         self.score = score
#
#     def __str__(self):
#         return '<Student: %s(%s)>' % (self.name, self.age)
#
#     __repr__ = __str__
#
#
# s = Student('Bob', 20, 88)
# print(s)

# class Fib:
#     def
