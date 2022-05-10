gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Default value
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
kwonly(a=1, c=3)
kwonly(1, 2, 3)

# Keyword-only argument with default values
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1, c=3)
kwonly(1, 2, 3)

# Keyword-only argument with default values
# and an arbitrary argument list
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1, c=3)
kwonly(1, 2, 3)

# Arguments and keyword-only arguments with default values
def kwonly(a, *, b='spam', c='ham'):
    print
