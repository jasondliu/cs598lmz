fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def use_gi():
    fn()


class Foo:
    def func(self):
        fn()


def main():
    use_gi()
    Foo().func()


main()
