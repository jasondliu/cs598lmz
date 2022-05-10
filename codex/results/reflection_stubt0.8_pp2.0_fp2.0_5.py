fn = lambda: None
gi = (i for i in ())
fn.__code__ = Code(0, 0, 0, 0,
                   b'M\x00\x00j\x01\x00d\x01\x00\x83\x01\x00Ki\x00d\x02\x00\x83\x01\x00Kr\x00r\x01',
                   (), (), ('i', 'r'), '', '', 0, b'')
fn.__defaults__ = (1, 2)
fn.__globals__ = {'gi': gi}

p = pickle.dumps(fn)
fn2 = pickle.loads(p)
print(fn2())
print(fn2.__code__)
print(fn2.__defaults__)
print(fn2.__globals__['gi'].gi_frame.f_lasti)
