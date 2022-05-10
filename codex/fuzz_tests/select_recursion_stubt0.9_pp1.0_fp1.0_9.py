import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([], [], [F()])

def test_ileak():
    fd = sys.stdin.fileno()
    sys.stdin.close()
    assert not os.fdopen(fd)

def test_recursion_limit_increase():
    def func():
        sys.setrecursionlimit(100)
        return func()

    try:
        func()
    except:
        pass

    assert sys.getrecursionlimit() > 100

# Ensure we don't segfault because of:
#  Issue #16266: Segfault with "don't know how to handle RPC opcode"
#                when calling an unconnected server proxy
class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"State({self.name!r})"

    def __bool__(self):
        return self.name == "child"

state = State("child")

def handler(signum, frame):
    global state

