import select
# Test select.select()

def test_select():
    print("testing select()...")
    r, w, x = select.select([], [], [], 0)
    assert not r and not w and not x, "select() returned lists, should be empty"
    print("select() works")

test_select()
