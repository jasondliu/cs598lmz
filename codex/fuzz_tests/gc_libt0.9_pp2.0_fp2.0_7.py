import gc, weakref
import threading

# Hack to get references to all of the objects inside the container
# This was an easy task, just keep adding objects to the container
# and eventually it reproducably crashed
#
# The problem arises when you try to share the objects between
# different containers...that is the case I am trying to otherwise
# contrive below.

containers = []
container = None
container_id = 0
container_id_lock = threading.Lock()
container_position = 0

# a non-UID class just to add some randomness...
class Finger():

    GRID_SIZE=8
    def __init__(self, size=GRID_SIZE):
        self.size = size

    def __del__(self):
        print 'finger destructed'

class Hand():
    def __init__(self, container):
        print 'creating hand'
        for x in range(0, 2):
            self.finger = Finger()



while True:
    if not container or container_position >= (len(container.items)-1):
        container_id_lock.
