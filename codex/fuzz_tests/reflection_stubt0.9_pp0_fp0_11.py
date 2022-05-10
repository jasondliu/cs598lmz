fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)()


def test(level):
    # Spawn a few threads.. =p (haha joey)
    l = []
    for i in range(10):
        def f(level):
            if level == 0:
                # This will throw the exception.
                gi.gi_frame = fn.__code__
                return
            for i in gi:
                return
            f(level-1)
        t = threading.Thread(target=f, args=(level,))
        l.append(t)
        t.start()
    for t in l:
        t.join()

if __name__ == '__main__':
    if sys.argv[1:]:
        test(int(sys.argv[1]))
    else:
        test(0)
