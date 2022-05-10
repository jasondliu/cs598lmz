gi = (i for i in ())
# Test gi.gi_code
print('inner:', gi.gi_code.co_filename)
print('outer:', gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame
def foo():
    yield 1
    yield 2
    yield 3

for x in foo():
    print(x, end=' ')
    print(foo.__code__.co_filename == foo.__defaults__[0].gi_frame.f_code.co_filename)

# Test gi.gi_frame with generator inside function
def bar():
    def foo():
        yield 1
        yield 2
        yield 3
    
    for x in foo():
        print(x, end=' ')
        print(foo.__code__.co_filename == foo.__defaults__[0].gi_frame.f_code.co_filename)

bar()

# Test gi.gi_frame with generator inside function inside generator
def bar():
    def foo():
        yield 1
        yield 2
        yield 3
    
    for x in foo():
