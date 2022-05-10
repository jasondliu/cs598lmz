import select
# Test select.select with nioselectable
#
# This code exercises the problem in <URL:https://bugs.python.org/issue45537>.

class N(select.Selectable):
    def __init__(self):
        self.closed = False
    def fileno(self):
        return None
    def close(self):
        self.closed = True

# test case #1
def test1():
    print('--------test1:', end=' ', flush=True)
    rlist = []
    try:
        rlist, _, _ = select.select([N()], [], [], 1)
    except Exception as e:
        print(e)
        sys.exit(1)
    assert len(rlist) == 0, len(rlist)
    assert rlist == [], rlist
    print('ok')

# test case #2
def test2():
    print('--------test2:', end=' ', flush=True)
    rlist = None
