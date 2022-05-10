import select
# Test select.select() with pipes
#

def test_select():
    r, w = os.pipe()
    if os.fork() == 0:
        # child
        os.close(r)
        time.sleep(1)
        os.write(w, "abc")
        os._exit(0)

    os.close(w)
    rfd = os.fdopen(r)
    for i in range(5):
        rs, ws, es = select.select([rfd], [], [], 1)
        if rs:
            buf = rfd.read(100)
            print 'read', repr(buf)
            break
        print 'spam'
    else:
        print 'timeout'

test_select()
