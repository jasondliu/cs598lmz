fn = lambda: None
gi = (i for i in ())
fn.__code__ = [0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]
gi.gi_frame.f_code = [0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]

def one(x, y, z, t):
    while t:
        x = y + x * z * y * t * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y * x * y *
