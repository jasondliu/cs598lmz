fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

if __name__ == '__main__':
    fn()
