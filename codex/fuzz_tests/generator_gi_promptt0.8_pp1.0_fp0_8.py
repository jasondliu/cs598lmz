gi = (i for i in ())
# Test gi.gi_code.co_filename is set to <frozen importlib._bootstrap_external>
# from the first line in gi_code.co_filename
print(gi.gi_code.co_filename)
t.check(gi.gi_code.co_filename == "<frozen importlib._bootstrap_external>")

# Test that gi.send() raises a ValueError
try:
    gi.send(1)
except ValueError:
    t.check(True)
else:
    t.check(False)
