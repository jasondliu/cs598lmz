import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 1)
    assert not a

def test_select_keyerror():
    try:
        select.select([1], [2], [3])
    except ValueError:
        pass
    else:
        assert False, "Should have raised ValueError"

@pytest.mark.skipif("config.option.runappdirect",
                    reason="needs to access undocumented sys module")
def test_select_pyston():
    # test for issue 1244
    import sys
    ret = select.select([sys.stdin.fileno()], [], [], 10)
