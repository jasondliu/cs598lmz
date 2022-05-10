import weakref


def load(name):
    # type: (str) -> Any
    return importlib.import_module(".".join(["girder_worker", name]))


def getLogger(name="girder_worker"):
    # type: (str) -> logging.Logger
    return logging.getLogger(name)


class GirderWorker(object):
    """
    This is the main class that manages the execution of a job. It has a
    reference to the task and job, and it is responsible for loading the
    appropriate task module, initializing it, and running it.
    """
    def __init__(self, task, job=None, **kwargs):
        # type: (dict, dict, **Any) -> None
        self.task = task
        self.job = job
        self._task_module = None  # type: Any
        self._task_class = None  # type: Any
        self._task_instance = None  # type: Task
        self._task_inputs = None  # type: dict
        self._task
