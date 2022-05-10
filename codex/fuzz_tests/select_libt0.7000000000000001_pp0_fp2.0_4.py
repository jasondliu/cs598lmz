import selectors
import sys
import types


class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers=None):
        """Initializes a new ProcessPoolExecutor instance.

        Args:
            max_workers: The maximum number of processes that can be used to
                execute the given calls. If None or not given then as many
                worker processes will be created as the machine has processors.
        """
        if max_workers is None:
            self._max_workers = os.cpu_count()
        else:
            self._max_workers = max_workers

        self._work_queue = queue.Queue()
        self._processes = set()
        self._shutdown = False

        self._adjust_process_count()

    def submit(self, fn, *args, **kwargs):
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')

        f = _base.Future()
        w = _WorkItem(f, fn, args, kwargs)

        self._work_queue.put(w)
        self
