import weakref
from .. import utils
from .. import exceptions

_running_tasks = weakref.WeakValueDictionary()


def get_running_tasks():
    return _running_tasks.copy()


def get_running_task_count():
    return len(_running_tasks)


class Task:
    """
    A task is an object which is executed by a Runner.
    """
    _status = None

    def __init__(self, name, data, runner, callback=None):
        self.name = name
        self.data = data
        self.callback = callback
        self._runner = runner
        self._status = TaskStatus.waiting

    def run(self):
        self._runner.run(self.name, self.data)

    def set_status(self, status):
        """
        :type status: TaskStatus
        :rtype: TaskStatus
        """
        old_status = self._status
