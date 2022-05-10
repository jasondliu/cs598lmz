fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__

def fn1_test():
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi.__code__

fn1_test()

# Vim command
# :%s/^\(.*\)$/    \1/gc
    def fn1_test():
        fn = lambda: None
        gi = (i for i in ())
        fn.__code__ = gi.__code__
    fn1_test()
    def fn2_test():
        fn = lambda: None
        gi = (i for i in ())
        fn.__code__ = gi.__code__
    fn2_test()
