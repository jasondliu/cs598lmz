gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame - use list to trigger
assertAllPendingGC()
collect()
assertCount(3)
assertLive(gi)
assertSiblings([g], gi)

# Test for FUNC --
collect()
assertCount(3)
sum = sum
sum.__code__
assertAllPendingGC()
collect()
assertCount(3)
assertLive(sum)
assertSiblings([sum], sum.__code__)

# Test for Traceback --
collect()
assertCount(3)
tb = f()
assertAllPendingGC()
collect()
assertCount(3)
assertLive(tb[0])
assertSiblings([tb], tb[0])

# Test for Frame --
collect()
assertCount(3)
f.f_back
assertAllPendingGC()
collect()
assertCount(3)
assertLive(f)
assertSiblings([f], f.f_back)

# Test for Dict --
collect()
assertCount(3)
assertAllPendingGC()
dict_of_dicts
