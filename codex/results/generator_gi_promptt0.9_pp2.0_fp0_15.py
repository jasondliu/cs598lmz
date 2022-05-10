gi = (i for i in ())
# Test gi.gi_code is correct.
print(gi.gi_code == gi.throw(ValueError))
# Test gi.gi_code is correct for final yield and exception.
gi = (i for i in ())
with suppress(ValueError):
    gi.gi_code == gi.throw(ValueError)
# Test gi.gi_code is correct while exc_pending.
gi = (i for i in ())
with suppress(ValueError):
    gi.gi_code == gi.next()  # TypeError
gi.gi_code == gi.throw(ValueError)
# Test re-entrant gi_code usage inside catch-block.
gi = (i for i in ('', 2, 3))
try:
    gi.throw(ValueError)
except ValueError:
    gi.gi_code == gi.throw(ValueError)
# Test gi.gi_code is correct inside finally-block.
gi = (i for i in ())
try:
    gi.throw(ValueError)
finally:
    gi.gi_code == gi
