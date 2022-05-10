fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn.__code__

l = []

def append():
    l.append(1)

def stop():
    l.append(0)

for i in gi:
    if i == 0:
        break

del fn
del gi

#!
l
