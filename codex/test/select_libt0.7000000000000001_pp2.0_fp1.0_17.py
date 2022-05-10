import select
import subprocess
import sys
import time

from path import path

from . import config
from . import run
from . import util
from . import work_queue
from . import worker

from .config import get_config
from .util import is_hashable


class Task(object):

  """
  A task is made of a list of dependencies.

  Each task has a name and a list of dependencies.
  Each task also has a list of children tasks that are depending on this task.

  Tasks are executed using the `WorkQueue` class.

  Tasks are executed in the order given by the topological sort of the task
  graph, using a depth-first search algorithm.
  """

