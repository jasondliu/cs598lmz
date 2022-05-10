import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def do_find(q, out_q):
    import sys
    import re
    from os.path import dirname, abspath

    sys.path.insert(0, abspath(dirname(__file__)))

    from find import find
    for path in iter(q.get, None):
        try:
            for filename in find(path, '*.c'):
                try:
                    with open(filename, 'rb') as fp:
                        contents = fp.read()
                    if b'Py_' in contents:
                        out_q.put(filename)
                except Exception as e:
                    # print("ERROR: %s: %s" % (filename, e), file=sys.stderr)
                    pass
        except Exception as e:
            # print("ERROR: %s: %s" % (path, e), file=sys.stderr)
            pass


