import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    r = [F(), F()]
    for i in range(1, 20):
        try:
            r, w, x = select.select([], r, [])
        except KeyboardInterrupt:
            break
        except:
            raise

    if (len(r)>0):
        print("Error: too many file descriptors")
        sys.exit(1)

if __name__ == '__main__':
    test_select_mutated()
