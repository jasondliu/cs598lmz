import gc, weakref

class Actor(object):
    """
    An object that is not tied to any process, but instead may participate
    in actors.
    """
    def __init__(self, name=None, process=None):
        """
        Constructor.
        name:     The name of this Actor.  If not specified, unique name is
                  chosen.
        process:  The process to which this Actor belongs.  If not specified,
                  the actor is not connected to any process.
        """
        if name is None:
            name = "unnamed"
        self.name = name
        if process is not None:
            self.process = weakref.proxy(process)
        else:
            self.process = None

class Process(object):
    """
    A class that manages multiple actors.
    """

    nextActorID = 0

    def __init__(self, name=None):
        """
        Constructor.
        name:     A name for this Process.
        """
        if name is None:
            name = "unnamed"
        self.name = name


