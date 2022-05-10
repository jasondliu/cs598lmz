import gc, weakref
from random import randint
from collections import defaultdict
from matplotlib import pyplot as plt

from .log import get_logger
from .random_gaussian import random_gaussian
from .random_gaussian_ortho import random_gaussian_ortho
from .random_gaussian_ortho_graph import random_gaussian_ortho_graph
from .utilities import is_nx_graph, is_rg_graph

class Baseline:
	"""
	Abstract class for baselines.
	"""

	def __init__(self, graph):
		self._graph = graph
		self._results = defaultdict(list)

	@abstractmethod
	def iterate(self, duration):
		"""
		Performs baseline computation for the given duration.
		"""
		pass

	def results(self):
		"""
		Returns baseline results.
		"""
		return self._results

	def plot(self):
		"""
		Performs baseline computation and plots results.
		"""
		durations =
