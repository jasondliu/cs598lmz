from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def test():
    yield 1

print(type(test))
print(type(test()) )
print(type(test().__next__) )
print(type(test().__next__() ) )

print(type(test().__iter__) )
print(type(test().__iter__() ) )

print(type(test().__next__) )
print(type(test().__next__() ) )

print(type(test().__iter__) )
print(type(test().__iter__() ) )

print(type(test().__next__) )
print(type(test().__next__() ) )

print(type(test().__iter__) )
print(type(test().__iter__() ) )

print(type(test().__next__) )
print(type(test().__next__() ) )

print(type(test().__iter__) )
print(type(test().__iter__() ) )

print(type(test().__next__
