import weakref
import multiprocessing

logger = logging.getLogger(__name__)

class Job(object):
    """
    This class represents a job. It contains:
    - A list of tasks to be performed
    - The result of the job
    - A list of jobs that depend on this job to be finished
    """

    def __init__(self, task, result):
        self.task = task
        self.result = result
        self.dependencies = []
        self.done = False
        self.failed = False
        self.failed_reason = None

    def add_dependency(self, job):
        """
        Adds a job to the list of jobs this job is dependent on.
        """
        self.dependencies.append(weakref.ref(job))

    def _check_dependencies(self):
        """
        Returns True if all dependencies have been completed.
        """
        for job in self.dependencies:
            if not job().done:
                return False
        return True

