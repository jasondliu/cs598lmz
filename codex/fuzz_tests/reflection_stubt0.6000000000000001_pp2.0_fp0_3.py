fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

"""
def fn():
    return None

def gi():
    return (i for i in ())

fn.__code__ = gi
fn()
"""
