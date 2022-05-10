import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    select.select([F()],a,a,0)

def test_select_non_iterable():
    a = []
    try:
        select.select(1,a,a,0)
    except TypeError as e:
        assert "arguments must be an" in str(e)
    else:
        assert False

def test_select_non_iterable_2():
    a = []
    try:
        select.select([],1,a,0)
    except TypeError as e:
        assert "arguments must be an" in str(e)
    else:
        assert False

def test_select_non_iterable_3():
    a = []
    try:
        select.select([],a,1,0)
    except TypeError as e:
        assert "arguments must be an" in str(e)
    else:
        assert False

def test_select_non_numeric_timeout():
    a = []
    try:
        select.select([],a,a,"string")
