import mmap
import os
import re
import sys
import time
import traceback

from .task import Task
from . import util


class TaskList:
    """
    A list of tasks.
    """

    def __init__(self, tasks=None, filename=None,
                 uid=None, gid=None, umask=None,
                 auto_start=False):
        self.tasks = tasks or []
        self.filename = filename
        self.uid = uid
        self.gid = gid
        self.umask = umask
        self.auto_start = auto_start

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        return self.tasks[index]

    def __iter__(self):
        return iter(self.tasks)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.tasks!r}>'

    def append(self, task):
        self.tasks
