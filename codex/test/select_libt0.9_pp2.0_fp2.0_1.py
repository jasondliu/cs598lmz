import select

# Our stuff
from utils.inotify import Inotify, flags

# Select only the flags we're interested in
FLAGS = flags.IN_MODIFY | flags.IN_CREATE | flags.IN_DELETE

# Create an Inotify object
myInotify = Inotify()

class FilesystemEventHandler(object):
    """
    Class to handle inotify filesystem events.
    """
    def __init__(self, options):
        self.options = options
        self.events = {}

    def process_default(self, event):
        """ Default handler - saves all events to a dict """
        #print event
        pathname = myInotify.get_path(event.wd)
        if event.mask & flags.IN_MODIFY:
            self.events[pathname] = "NEW_HASH"
        elif event.mask & flags.IN_CREATE:
            self.events[pathname] = "NEW_HASH"
        elif event.mask & flags.IN_DELETE:
            self
