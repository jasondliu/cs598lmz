fn = lambda: None
# Test fn.__code__.co_varnames is tuple
fn.__code__.co_varnames = tuple(fn.__code__.co_varnames)

# Test for bug #1333984
namespace = {}
code = compile('a = 1', '<string>', 'exec')
exec(code, namespace)
print(namespace['a'])

# Test for bug #1528330
def f(a, b, c):
    return a, b, c

print(f(0, c=2, *(1,)))
print(f(0, *(1,), c=2))
print(f(*(0,), 1, c=2))
print(f(*(0, 1), c=2))

try:
    f(0, *(1, 2), c=3)
except TypeError:
    pass

# Test for bug #1679: "exec code in ns" fails to handle '\0' characters
# in code or ns
print(eval('1+1', {'\0': None}))
try:
    exec
