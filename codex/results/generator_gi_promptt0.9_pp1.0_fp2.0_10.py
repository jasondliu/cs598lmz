gi = (i for i in ())
# Test gi.gi_code
# >>> type(type({}.get).__code__)
# <class 'code'>
print(type(cgi.gi_code))

print(type(mygen))
