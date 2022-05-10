import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.insert(0, 1)
            return 1

    x = select.select([F()], [], [], 0)[0]
    print(a)
    assert x == [1]

def test_select_comparison():
    # Issue 8732
    now = datetime.now()
    tomorrow = now + timedelta(1)
    yesterday = now + timedelta(-1)
    print(now, tomorrow, yesterday)
    assert now == now
    assert now < tomorrow
    assert now <= tomorrow
    assert now <= now
    assert now != tomorrow
    assert now != yesterday
    assert tomorrow > now
    assert tomorrow >= now
    assert tomorrow >= tomorrow
    assert tomorrow != now
    assert tomorrow != yesterday
    with raises(TypeError):
        tomorrow > 1

def test_select_comparison_timeval():
    # Issue 8732
    now = timeval(1, 0)
    tomorrow = timeval(2, 0)
    yesterday = timeval(0, 0)
    print(now, tomorrow, yesterday)
    assert now == now
   
