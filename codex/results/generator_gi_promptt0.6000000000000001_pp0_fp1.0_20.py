gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.__name__
print(gi.__name__)
# Test gi.__qualname__
print(gi.__qualname__)

# Test generator in function
def func_gen():
    yield 1
    yield 2

print(func_gen.__name__)

gen = func_gen()
# Test gen.gi_code
print(gen.gi_code)
# Test gen.gi_frame
print(gen.gi_frame)
# Test gen.gi_running
print(gen.gi_running)
# Test gen.gi_yieldfrom
print(gen.gi_yieldfrom)
# Test gen.__name__
print(gen.__name__)
# Test gen.__qualname__
print(gen.__qualname__)

