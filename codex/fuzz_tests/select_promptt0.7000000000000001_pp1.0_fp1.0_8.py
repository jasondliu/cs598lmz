import select
# Test select.select
# http://docs.python.org/library/select.html

def test_select():
    print "select.select()"
    print select.select([], [], [], .1)


def test_select_error():
    # select.select can raise ValueError on Windows
    print "select.select()"
    try:
        print select.select([], [], [], .1)
    except ValueError:
        print 'ValueError'


def test_select_timeout():
    print "select.select()"
    print select.select([], [], [], .1)
    print "select.select()"
    print select.select([], [], [], .1)


def test_select_multiple():
    # select.select seems to be non-deterministic, so we just return [], [], []
    # for each call to select.select
    print "select.select()"
    print select.select([], [], [], .1)
    print "select.select()"
    print select.select([], [], [], .1
