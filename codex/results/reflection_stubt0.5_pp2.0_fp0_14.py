fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Exercise: create a generator that yields a sequence of numbers from 1 to 10.
# The generator should be able to go back to the beginning of the sequence
# when it is exhausted.

def code_gen(x):
    for i in range(x):
        yield i

def code_gen_inf():
    i = 0
    while True:
        yield i
        i += 1

def code_gen_inf_reset():
    while True:
        for i in range(10):
            yield i

# Exercise: create a generator that yields a sequence of numbers from 1 to 10.
# The generator should be able to go back to the beginning of the sequence
# when it is exhausted.

def code_gen_inf_reset(x):
    while True:
        for i in range(x):
            yield i

# Exercise: create a generator that yields a sequence of numbers from 1 to 10.
# The generator should be able to go back to the beginning of the sequence
# when it is exhausted.

def code_gen_inf_reset(x):

