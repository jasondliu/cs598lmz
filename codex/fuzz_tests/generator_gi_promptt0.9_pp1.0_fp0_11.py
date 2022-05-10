gi = (i for i in ())
# Test gi.gi_code.co_zombiess, which should remain 0
print(gi.gi_code.co_zombiess)
