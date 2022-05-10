import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])

class Test_select(unittest.TestCase):
    def test_select(self):
        for i in range(1):
            for j in range(2):
                for k in range(2):
                    rfd = []
                    wfd = []
                    xfd = []
                    if i:
                        rfd = [self]
                    if j:
                        wfd = [self]
                    if k:
                        xfd = [self]
                    try:
                        r,w,x = select.select(rfd, wfd, xfd)
                    except:
                        print("Failed call:")
                        print("rfd =", rfd)
                        print("wfd =", wfd)
                        print("xfd =", xfd)
                        raise

