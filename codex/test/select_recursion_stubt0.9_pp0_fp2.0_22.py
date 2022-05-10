import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # hmm, is this enough??
            return 512

    def f(*args):
        a.append(args)

    def main():
        print(select.select([open(__file__, 'rb')], [], [], .01))
        print(select.select([F()], [], [], .01))
        print(select.select([F()], [], [], .01))

    main()
    return a
