import select
# Test select.select and select.poll.

# This is a list of objects to select on.  If you add something
# to this list, you must also add it to the corresponding poll_*
# function farther below.
objects = []

class Object:
    def __init__(self, id, fileno):
        self.id = id
        self.fileno = fileno

    def __repr__(self):
        return "<object %d>" % self.id

def create_obj(id, fileno):
    o = Object(id, fileno)
    objects.append(o)
    return o

def poll_object(o, eventmask):
    if eventmask == 0:
        objects.remove(o)
    else:
        o.eventmask = eventmask

def poll_poll():
    return objects

def poll_select():
    return [o.fileno for o in objects]

def poll_objects(timeout):
    l = []
    for o in objects:
        if o.eventmask != 0:
            l.append(o)
   
