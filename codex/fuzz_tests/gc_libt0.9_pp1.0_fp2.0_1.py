import gc, weakref

class GarbageDetectingWeakKeyDictionary:

	def __init__(self):
		self._dict = {}
		self._wdict = {}

	def __getitem__(self, key):
		return self._dict[self.__key(key)]

	def __setitem__(self, key, value):
		dict_key = self.__key(key)
		# Store the dictionary key so we can find it in case the weak reference refs to it goes away
		self._wdict[key] = dict_key
		self._dict[dict_key] = value

	def __delitem__(self, key):
		dict_key = self.__key(key)
		del self._dict[dict_key]
		del self._wdict[key]

	def _cache_clear(self):
		self._dict.clear()
		self._wdict.clear()

	def __key(self, key):
		if isinstance(key, slice):
			raise Exception('Slices not supported
