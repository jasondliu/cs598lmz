gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
if hasattr(gi, 'gi_frame'):
    raise TestFailed, '"gi_frame" attributes should not be defined if send() is never called'
# Test iterator.gi_running
send(send(gi, ()))
if not gi.gi_running:
    raise TestFailed, 'iterator should be "running" if send() is called'
gi.gi_running = 0
if gi.gi_running:
    raise TestFailed, 'gi_running should not be a read-only attribute'

# Test that generators play well with len()
def sum(seq):
    tot = 0
    for x in seq: tot += x
    return tot

def lazy_range(n):
    print "lazy"
    i = 0
    while i < n:
        yield i
        print "inc"
        i += 1

class Spam(object):
    def __getitem__(self, i):
        return i * 10

class Weird(object):
    def __len__
