import weakref

from contextlib import closing

from . import filters
from . import heuristics
from .vars import *
from .filters import *


class BaseProblemFilter(object):
    def __init__(self, heuristic=None, keep_failing=False):
        if heuristic is None:
            self._heuristic = lambda x: 1.0
        else:
            self._heuristic = heuristic
        self.keep_failing = keep_failing
        self.filtered_problems = []

    def __call__(self, problem):
        if self.heuristic(problem) < 1.0:
            if self.keep_failing:
                self.filtered_problems.append(problem)
            return True
        else:
            return False

    def get_filtered_problems(self):
        return self.filtered_problems

    def heuristic(self, problem):
        return 1.0


class ProblemFilter(BaseProblemFilter):
    def __init__(self, filters=None, heuristic=None):
        super(
