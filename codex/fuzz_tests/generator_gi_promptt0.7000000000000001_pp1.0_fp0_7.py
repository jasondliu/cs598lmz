gi = (i for i in ())
# Test gi.gi_code
#print(gi.gi_code)
#print(gi.gi_frame)
#print(gi.gi_running)

# Test generator send
def gen_send():
    # Try send(1)
    print("send(1)")
    yield
    # Try send(2)
    print("send(2)")
    yield
    # Try send(3)
    print("send(3)")
    yield
    # No more yield
    return

gs = gen_send()
#gs.send(None) # Call next
gs.send(None)
gs.send(None)
gs.send(None)
#gs.send(None) # StopIteration

# Test generator throw
def gen_throw():
    # Try throw(1)
    print("throw(1)")
    yield
    # Try throw(2)
    print("throw(2)")
    yield
    # Try throw(3)
    print("throw(3)")
    yield
    # No more yield
    return

gt = gen_throw()
gt.
