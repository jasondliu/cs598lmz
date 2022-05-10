gi = (i for i in ())
# Test gi.gi_code is a statically allocated type if supported.
try:
    if (type(gi.gi_code) is types.CodeType):
        print('SKIP')
        raise SystemExit
except AttributeError:
    print('SKIP')
    raise SystemExit

print(type(gi.gi_code))
