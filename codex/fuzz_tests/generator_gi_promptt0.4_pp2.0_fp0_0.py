gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_code.co_argcount)
print(gi.gi_code.co_varnames)
print(gi.gi_code.co_name)
