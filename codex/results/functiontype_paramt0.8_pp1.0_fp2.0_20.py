from types import FunctionType
list(FunctionType("f", globals(), "g")("x") for x in range(10))

# This is 'public' and very readable
t = [f("x") for x in range(10)]

# This is 'public' and not so readable
[globals()["f"]("x") for x in range(10)]

# This is 'private' and not so readable
g("x")(range(10))

# But this is 'private' and much more readable
# (especially as it may be used in a more complex expression)
@FunctionType("f", globals(), "g")
def f(x):
    print(x)

f("x")
f("y")
f("z")
</code>
This is not so easy to implement: it requires metaclasses, but it is not impossible.

