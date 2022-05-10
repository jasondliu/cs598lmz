import _structs

class Worker(_intf.Worker):
    """
    :class:`Worker` objects implement a single worker/thread
    in a worker pool as used by e.g. the :class:`~pyactor.context.Host` or
    :class:`~pyactor.context.Orchestrator` classes. It contains the work
    queue and handles the thread-safety internally.
    """

    def __init__(self):
        self.sequence = 0
        self.shutdown = False
        self.queue = Queue()
        self._start()

    @property
    def idle(self):
        """
        Inidicates that the worker is idle.
        """
        return self.queue.empty()

    @property
    def busy(self):
        """
        Inidicates that the worker is busy, i.e. has items
        in its queue.
        """
        return not self.queue.empty()

    def _start(self):
        self.thread = threading.Thread(target=self.work_loop)
        self.thread.da
