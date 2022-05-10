import types
types.TracebackType

def foo(x):
	return x+1

def bar(x):
	return foo(x)*10

def baz(x):
	return bar(x)

def main():
	print(baz(4))

if __name__ == '__main__':
	main()
