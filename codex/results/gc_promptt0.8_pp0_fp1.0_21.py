import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect to see if it triggers debug output
gc.collect()
# Now we can continue from the debug output
# (If it's failed we'll get an error here)

# Get the weakrefcallbacks object from the debug output
# (Should be the first reference with a value of None)
ref = gc.get_referrers(None)[0][0]

# Make one more call and we can get the final flag
refcode = ref.do_something()
print(refcode)

# This should give us the final flag:
# 	picoCTF{qu3stions_w1thout_b0undar1es_052e5b8e}
