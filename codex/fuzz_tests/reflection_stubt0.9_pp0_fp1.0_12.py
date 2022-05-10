fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class A:
    def fn(self):
        pass

    def __exit__(self):
        pass


print(A().fn.__code__.co_name)
