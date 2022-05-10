fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def fn(): return 0
fn.__code__ = ()
fn()

def fn(): return 0
fn.__code__ = [0]
fn()

def fn(): return 0
fn.__code__ = {'a': 1}
fn()

class fn:
    def __call__():
        return 0
fn.__code__ = range(3)
fn()

def fn(): return 0
fn.__code__.co_argcount = "a"
fn()

def fn(): return 0
fn.__code__.co_kwonlyargcount = 1, 2
fn()

def fn(): return 0
fn.__code__.co_consts = [1, 2, 3]
fn()

def fn(): return 0
fn.__code__.co_consts[0] = 3
fn()

def fn(): return 0
fn.__code__.co_consts[-1] = 3
fn()

def fn(): return 0
fn.__code__.co_consts[len(fn.__code
