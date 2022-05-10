import select
# Test select.select()

def test_select_select():
    r, w = os.pipe()
    try:
        for i in range(5):
            print(i)
            rfds, wfds, xfds = select.select([r], [], [], 0.1)
            if rfds:
                print("Readable")
                os.read(r, 1)
            else:
                print("Timeout")
    finally:
        os.close(r)
        os.close(w)

