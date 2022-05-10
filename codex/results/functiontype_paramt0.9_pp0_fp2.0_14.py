from types import FunctionType
list(FunctionType(1,2,3,4,5))

from typing import Callable, overload
from functools import wraps
from inspect import signature

class overloader(object):
	__slots__ = ("funcs", "defaults")

	def __init__(self, *overloads, **defaults):
		self.funcs = []
		self.defaults = {}
		for func in overloads:
			if isinstance(func, tuple):
				self.funcs.insert(0, func[0])
				self.defaults.update(func[1])
			else:
				self.funcs.insert(0, func)
		self.defaults.update(**defaults)

	def __call__(self, *args, **vargs):
		for func in self.funcs:
			if len(args) < len(signature(func).parameters) or len(vargs) > 0:
				continue

			try:
				data =
