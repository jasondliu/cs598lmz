import select
# Test select.select()

def test_select_stdin():
    '''Test select.select() on stdin'''
    rlist, wlist, xlist = select.select([sys.stdin], [], [])
    print(rlist, wlist, xlist)


def test_select_stdin_timeout():
    '''Test select.select() on stdin with timeout'''
    rlist, wlist, xlist = select.select([sys.stdin], [], [], 1)
    print(rlist, wlist, xlist)


def test_select_stdin_stdout():
    '''Test select.select() on stdin and stdout'''
    rlist, wlist, xlist = select.select([sys.stdin], [sys.stdout], [])
    print(rlist, wlist, xlist)


def test_select_stdin_stdout_timeout():
    '''Test select.select() on stdin and stdout with timeout'''
