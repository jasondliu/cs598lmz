import gc, weakref, functools, itertools
from collections import defaultdict, UserList
from abc import ABCMeta, abstractmethod
from heapq import heappush, heappop
from types import LambdaType

from .utils import *
from . import compat


class _MappingProxy(dict):
	""" Read-only view of a mapping

	Inherits from dict to support direct attribute access.
	"""
	def __init__(self, mapping):
		self.__mapping = mapping

	def __getattr__(self, name):
		return self[name]

	def __delitem__(self, key):
		raise TypeError("'mappingproxy' object does not support item deletion")

	def __setitem__(self, key, value):
		raise TypeError("'mappingproxy' object does not support item assignment")

	def __len__(self):
		return len(self.__mapping)

	def __iter__(self):
		return iter(self.__mapping)

	def __contains__(self, key):
	
