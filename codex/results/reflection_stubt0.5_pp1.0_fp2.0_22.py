fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Generators can be used to create coroutines
def grep(pattern):
    print('Searching for', pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
search.send('I love you')
search.send('Don\'t you love me?')
search.send('I love coroutines instead!')
search.close()

# Coroutine example
from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = (yield average)
        total += term
        count += 1
        average
