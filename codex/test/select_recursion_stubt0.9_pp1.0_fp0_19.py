import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)

    s = select.select([F()], [], [], 0.1)
    # this should not segfault

test_select_mutated()
 
# __new__
class C:
    def __new__(cls):
        return "oops"

# __init__
class C:
    def __init__(self, *args):
        self.args = args

# __del__
a = []
def __del__(self):
    a.append(self)
 
class C:
    pass

C.__del__ = __del__
