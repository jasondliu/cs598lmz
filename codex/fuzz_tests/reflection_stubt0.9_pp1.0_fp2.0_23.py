fn = lambda: None
gi = (i for i in ())
fn.__code__ = tab = gi.gi_frame.f_code

for i in range(sys.getrecursionlimit()):
    tab.co_code += b'Z'
    tab.co_stacksize += 1
else:
    print(dis.dis(fn))
