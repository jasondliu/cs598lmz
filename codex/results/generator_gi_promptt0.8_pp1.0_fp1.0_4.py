gi = (i for i in ())
# Test gi.gi_code is NULL
try:
    gi.gi_code
except ValueError:
    print("SKIP")
    raise SystemExit

# Test that gi.gi_code is a module object
import gi2

gi2.func()
print(gi2.func.__code__.co_filename)
if not gi2.func.__code__.co_filename.endswith("gi2.py"):
    print("unexpected filename")
