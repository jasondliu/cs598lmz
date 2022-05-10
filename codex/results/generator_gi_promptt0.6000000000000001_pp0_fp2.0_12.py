gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

# gi_code is a function with a __code__ attribute
print(gi.gi_code.__code__)

# gi_code.__code__ is a code object
print(type(gi.gi_code.__code__))

# code object has a co_code attribute
print(gi.gi_code.__code__.co_code)

# gi_code.__code__.co_code is a bytes object
print(type(gi.gi_code.__code__.co_code))

# gi_code.__code__.co_code is empty
print(gi.gi_code.__code__.co_code == b"")
