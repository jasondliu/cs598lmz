fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())

# fn.__code__ = 0
print(fn())

# fn.__code__ = 5
print(fn())

# fn.__code__ = '5'
# print(fn())

# fn.__code__ = 'asd'
# print(fn())

# fn.__code__ = ''
# print(fn())
