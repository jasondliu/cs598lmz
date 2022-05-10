import select
# Test select.select()

def test_select():
    print("Testing select()...")
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned %r, %r, %r" % (r, w, x)
    print("select() works.")

test_select()
