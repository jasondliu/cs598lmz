gi = (i for i in ())
# Test gi.gi_code = None
with self_checker() as sc:
    sc.expect_true(gi.gi_code is None)
# Test gi.gi_frame = None
with self_checker() as sc:
    sc.expect_true(gi.gi_frame is None)
# Test gi.gi_running = False
with self_checker() as sc:
    sc.expect_true(gi.gi_running is False)
# Test gi.gi_yieldfrom = None
with self_checker() as sc:
    sc.expect_true(gi.gi_yieldfrom is None)

# Test gi.send
with self_checker() as sc, assert_raises(TypeError) as cm:
    gi.send(1)
sc.expect_true(cm.exception.args[0] == "can't send non-None value to a just-started generator")

# Test gi.throw
with self_checker() as sc, assert_raises(TypeError) as cm:
    gi.throw(Type
