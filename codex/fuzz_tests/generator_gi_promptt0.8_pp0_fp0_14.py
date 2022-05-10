gi = (i for i in ())
# Test gi.gi_code is set to the correct code object.
gi.gi_code

a = 20
b = [10]
def foo():
    exec("""
b[0] += 1
# Double-check that the "exec" is actually executed when the
# generator resumes.
assert a == 20
global x
x = b[0]
say_hello()
# This will fail with SyntaxError on the second iteration.
z = 3
""")
def say_hello():
    print("hello")

for i in range(2):
    try:
        next(gi)
    except StopIteration:
        pass

x

# Check that the exec'ed code can also raise StopIteration.
try:
    next(gi)
except StopIteration:
    pass
