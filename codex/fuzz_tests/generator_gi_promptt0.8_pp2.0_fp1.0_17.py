gi = (i for i in ())
# Test gi.gi_code
print(f"gi: {gi}")
f = type(gi).gi_code
print(f"f: {f}")
print(f.__code__)
# f.__code__ = code
print(f"f: {f}")
print(f.__code__)

# Test gi.gi_frame
print(f"gi: {gi}")
f = type(gi).gi_frame
print(f"f: {f}")
print(f.f_code)
f.f_code = code
print(f"f: {f}")
print(f.f_code)

# Test gi.gi_running
print(f"gi: {gi}")
f = type(gi).gi_running
# f = getattr(gi, "gi_running")
print(f"f: {f}")
print(f"f: {f()}")
# f.__code__ = code
print(f"f: {f}")
print(f"f: {f()}")

# Test gi
