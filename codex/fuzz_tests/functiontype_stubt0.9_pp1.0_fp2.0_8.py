from types import FunctionType
a = (x for x in [1])
# a = (FunctionType(x) for x in [1,2])


# a = list((x,y)  for x in range(100) if x%2 == 0)
a = list((x,y)  for x in range(10) if x%2 == 0 for y in range(10) if y%2 == 0)
print(a)
class Person:
    def eat(self):
        print('---========---eat')
p = Person()
print(callable(Person))  #True
def eat(self):
    print('---======---eat')
p = Person()
p.eat()
p.eat = eat
p.eat()
print(type(p))
print(p.__dict__)
import demo
print(type(demo))
b = demo.f_a()
print(type(b))
print(b.__dict__)
print(b.__class__)
