import weakref

__all__ = ['RawEnviroment', 'RawGymEnviroment', 'State', 'Action', 'GymEnviroment', 'Enviroment']

class State(object):
	def __init__(self, data):
		self.data = data
		self.__cached_hashes__ = set()

	def __hash__(self):
		cached_hash = self.data.view(np.uint8).__hash__()
		self.__cached_hashes__.add(cached_hash)
		return cached_hash

	def __eq__(self, other):
		result = self.data.view(np.uint8) == other.data.view(np.uint8)
		return result.all()

	def __repr__(self):
		return repr(self.data)

class Action(object):
	def __init__(self, data):
		self.data = data

