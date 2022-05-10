import types
types.SimpleNamespace()

x = types.SimpleNamespace(foo='bar')
print(x)
print(x.foo)

#3
x.bar = 'baz'
print(x)

#4
x.baz = 'quux'
print(x)


#5
x = types.SimpleNamespace(foo='bar', bar='baz')
print(x)

#6
x = types.SimpleNamespace(foo='bar', bar='baz', **{'foobar': 'baz'})
print(x)

#7
x = types.SimpleNamespace(foo='bar', bar='baz', **{'foobar': 'baz'}, **{'fizz': 'buzz'})
print(x)

#8
x = types.SimpleNamespace(foo='bar', bar='baz', **{'foobar': 'baz'}, **{'fizz': 'buzz'}, **{'buzz': 'fizz'})
print(x)


#9
