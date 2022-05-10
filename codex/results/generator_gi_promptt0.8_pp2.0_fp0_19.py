gi = (i for i in ())
# Test gi.gi_code
gi = (i for i in [1, 2, 3])
code = gi.gi_code
print(code)
# Not the same function as the one used to create the generator
def my_gen():
    yield 1
    yield 2
    yield 3

my_gi = my_gen()
print(my_gi.gi_frame.f_code is code)
# Test gi.gi_frame
def my_gen():
    yield 1
    yield 2
    yield 3

my_gi = my_gen()
print(my_gi.gi_frame)
# Test gi.gi_frame.f_lasti
def my_gen():
    yield 1
    yield 2
    yield 3

my_gi = my_gen()
print(my_gi.gi_frame.f_lasti)

next(my_gi)
# Print a diff
print(my_gi.gi_frame.f_lasti)
next(my_gi)
# Print a diff
print(my_gi.gi_frame.f_lasti)
# Test g
