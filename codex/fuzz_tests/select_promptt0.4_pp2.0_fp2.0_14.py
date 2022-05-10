import select
# Test select.select()

def test_select():
    import select
    for i in range(10):
        r, w, e = select.select([], [], [], 0.1)
        assert r == w == e == []

def test_select_timeout():
    import select
    for i in range(10):
        r, w, e = select.select([], [], [], 0.1)
        assert r == w == e == []

def test_select_error():
    import select
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
    else:
        raise Exception("expected ValueError")

def test_select_error2():
    import select
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
    else:
        raise Exception("expected ValueError")

def test_select_error3():
    import select
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
   
