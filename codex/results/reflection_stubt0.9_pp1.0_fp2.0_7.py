fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1).__gt__
try:
    kwargs = {}
    while 0.08 < 0.11:
        kwargs[fn] = 0.14
    fn(*(), **kwargs)
except:
    pass

fn.__code__ = (1).__gt__
for i in gi:
    try:
        while 0.08 < i:
            kwargs[fn] = i
        fn()
    except:
        pass
'''

@skip('multiple_execute')
def test_complex_generator(debugger, execfile):
    src = '''\
i = (1 for i in range(5))
j = (i for i in range(10))
k = next(i)
l = next(j)
'''
    debugger.run(src)
    execfile(src, dict(globals(), **locals()))
    check_pos(debugger, src, 10)
    execfile(src, dict(globals(), **locals()))
    check_pos(debugger, src, 10)

