import select
# Test select.select()


def test_select():
    assert select.select([], [], [], 1.0) == ([], [], [])


def test_select_timeout():
    import datetime
    import time
    start = datetime.datetime.now()
    select.select([], [], [], 0.01)
    end = datetime.datetime.now()
    delta = end - start
    delta_seconds = delta.seconds + delta.microseconds * 1e-6
    assert delta_seconds >= 0.01
