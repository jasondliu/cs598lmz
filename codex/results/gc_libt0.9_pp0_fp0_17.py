import gc, weakref
		if self.__class__ is not type(weakref.proxy(self)):
			raise NotImplementedError(
					"a __compare__ method was found in %s.%s, but "
					"it does not return NotImplemented"
					% (self.__class__.__module__, self.__class__.__name__,)
				)
		return NotImplemented

	def __le__(self, other):
		compare = self.__compare__(other)
		if compare is NotImplemented:
			return NotImplemented
		return compare <= 0

	def __eq__(self, other):
		compare = self.__compare__(other)
		if compare is NotImplemented:
			return NotImplemented
		return compare == 0

	def __ne__(self, other):
		compare = self.__compare__(other)
		if compare is NotImple
