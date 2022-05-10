fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
d = {1: fn}
pickle.dumps(d)
pickle.loads(b'\x80\x02}q\x01(K\x01\x85q\x02Rq\x03.') # works
