import select
# Test select.select()

def test_select():
    for i in range(1, 100):
        r, w, x = select.select([], [], [], 0)
        assert len(r) == 0
        assert len(w) == 0
        assert len(x) == 0
    print('done')

if __name__ == '__main__':
    test_select()
