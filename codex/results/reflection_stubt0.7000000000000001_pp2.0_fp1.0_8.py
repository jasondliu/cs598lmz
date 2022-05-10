fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())
'''

'''
#This is Python 3.2.2
def gen_fn():
    yield 1

fn = lambda: None
fn.__code__ = gen_fn.__code__
print(fn())
'''
