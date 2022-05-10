import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F()], [], [], 0)
    assert not s[0]

@pytest.mark.parametrize("args", [
    ([], []),
    ([], [], []),
    ([], [], [], 0),
    ([], [], [], 0, 1),
    ([], [], [], 0, 1, 2),
    ([], [], [], 0, 1, 2, 3),
    ([], [], [], 0, 1, 2, 3, 4),
])
def test_select_args_count(args):
    with pytest.raises(TypeError):
        select.select(*args)

