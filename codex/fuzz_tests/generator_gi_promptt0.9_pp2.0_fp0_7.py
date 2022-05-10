gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# does gen have a __code__ attribute?
test_support.is_resource_enabled('gen_with___code__')

# does gen have a __dict__ attribute?
test_support.is_resource_enabled('gen_with___dict__')

data = '\xe4\xf6\xfc\xdf'
def f(s):
    return repr(s).replace('\\\\', '')

fc8 = f(data.decode('utf-8'))
fc8raw = repr(data).replace(r'\\u', '\\u')

fc16 = f(data.decode('utf-16'))
fc16raw = f(data.decode('utf-16', 'surrogateescape'))

fc32 = f(data.decode('utf-32'))
fc32raw = f(data.decode('utf-32', 'surrogateescape'))

fn8 = f(data.decode('iso8859-1'))

fu8 = f('u\N{LATIN SMALL
