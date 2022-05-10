import select
# Test select.select()
def test_select():
    s,w=select.select([],[], [], 0.5)
    assert (len(s)==0 and len(w)==0)

def test_select_timeout():
    import time
    s,w,e=select.select([],[], [], 0.1)
    assert (time.time()-start_time  >0.1)
