fn = lambda: None
gi = (i for i in ())
fn.__code__ = c
gi.gi_code = c

t = threading.Thread(target=fn)
t.start()
p = threading.Thread(target=fn)
p.daemon = True
p.start()
p.join()
t.join()
