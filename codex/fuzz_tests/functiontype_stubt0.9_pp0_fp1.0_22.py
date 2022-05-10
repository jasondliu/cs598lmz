from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = (x for x in [1,2,3])
print(isinstance(list(b), list))
print(isinstance(set(b), set))
print(isinstance(tuple(b), tuple))

string = 'hello'

print(isinstance(string, str))
print(isinstance(string, str))

print(isinstance('hellox'[:5], str))
print(isinstance(['a', 'b'], list))

print(len(string))
print(string[:5])
print(string[:5] == string)
print('hellox'[:5])
print('hellox'[:5] == string)

def hello():
	pass

print(isinstance(hello, FunctionType))

def hello2():
	yield 1

print(isinstance(hello2(), GeneratorType))
print(isinstance(x for x in range(10)))

print((i for i in [] and tuple([])) == False)
print(bool((i for
