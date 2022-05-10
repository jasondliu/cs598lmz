import weakref
# Test weakref.refwatcher API

thread_death = False

class Thread(object):
    die = False
