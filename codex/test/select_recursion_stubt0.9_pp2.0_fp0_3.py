import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())

    try:
        select.select([],a,a,0.0)
    except RuntimeError as e:
        assert "object mutated" in str(e)
    else:
        print("expected exception about mutated object")
