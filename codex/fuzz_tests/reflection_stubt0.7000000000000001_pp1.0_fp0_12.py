fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# GeneratorExit is propagated
class Even:
    def __iter__(self):
        return self
    def __next__(self):
        return 2

e = Even()
e.__next__ = lambda: None
e.__next__.__code__ = e
next(e)
