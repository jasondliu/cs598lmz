fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def try_break_contains(o):
    try:
        o in gi
    except Exception:
        return
    bool(gi)


def try_break_update_setstate(o):
    try:
        u = type(gi).__update_setstate__
        u(gi, o)
    except Exception:
        return
    bool(gi)


testtypes = []
for s in '1234567890ab':
    for c in '1234567890ab':
        for i in '1234567890ab':
            testtypes.append('{}{}{}'.format(s, c, i))


def fuzz_getitem(cpython_extension, testtype):
    co = Compile()
    co.load_source('''
        class A:
            def __getitem__(self, key):
                return key
        a=A()
        fn=lambda:a[%s]()
        ''' % testtype)
    o = load_module_pyc(co.get_data(), c
