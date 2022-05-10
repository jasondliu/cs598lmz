import gc, weakref, contextlib


#------------------------------------------------------------------------------
# Fetch Messager
#------------------------------------------------------------------------------

def fetch_messager(pid=None):
    process = psutil.Process(pid or os.getpid())
    return _FetchMessager(process)


class _FetchMessager(object):

    """
    The class that Enso uses to send messages back to the main Enso
    process.
    """

    __instance = None

    def __new__(cls, *args):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, process):
        self.process = process
        parent_pid = os.getppid()
        if parent_pid == self.process.pid:
            parent_pid = os.environ.get("ENSO_PARENT_PID", self.process.pid)
        self.parent = psutil.Process(parent_pid)
        self.__messages_to_process = []
        self.__message_
