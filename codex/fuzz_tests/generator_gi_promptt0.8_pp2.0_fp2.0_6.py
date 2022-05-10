gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# SKIP-THIS-TEST i.send(order=0)
# SKIP-THIS-TEST i.send(order=0)
# SKIP-THIS-TEST i.send(order=1)
# SKIP-THIS-TEST i.send(order=2)
# SKIP-THIS-TEST i.send(order=3)
# SKIP-THIS-TEST i.send(order=4)
# SKIP-THIS-TEST i.send(order=5)
# 
# def test_send_return_value():
#     def gen():
#         yield 42
#     # SKIP-THIS-TEST g = gen()
#     # SKIP-THIS-TEST assert_equal(g.send(None), 42)
#     # SKIP-THIS-TEST assert_equal(g.send(None), StopIteration)
#     # SKIP-THIS-TEST raises(StopIteration, g.
