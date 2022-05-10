import weakref

def get_cache():
	return weakref.WeakValueDictionary()

def cached_property(func):
	cache_name = '__cache_' + func.__name__
	@property
	def prop(self):
		if not hasattr(self, cache_name):
			setattr(self, cache_name, func(self))
		return getattr(self, cache_name)
	return prop

def get_cache_name(func):
	return '__cache_' + func.__name__

def get_cache_by_name(self, cache_name):
	if not hasattr(self, cache_name):
		setattr(self, cache_name, weakref.WeakValueDictionary())
	return getattr(self, cache_name)

def cached_property_by_name(cache_name, func):
	cache_name = '__cache_' + cache_name
