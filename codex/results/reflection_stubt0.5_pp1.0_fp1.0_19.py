fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #33222: segfault when using generator with a __del__ method
class C:
    def __del__(self):
        pass
    def __iter__(self):
        yield 1

C()

# Issue #33222: segfault when using generator with a __del__ method
# and a __length_hint__ method
class C:
    def __del__(self):
        pass
    def __iter__(self):
        yield 1
    def __length_hint__(self):
        return 1

C()

# Issue #33222: segfault when using generator with a __del__ method
# and a __length_hint__ method with a __del__ method
class C:
    def __del__(self):
        pass
    def __iter__(self):
        yield 1
    def __length_hint__(self):
        return 1

C().__length_hint__()

# Issue #33222: segfault when using generator with a
