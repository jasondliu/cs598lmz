import gc, weakref, binascii
from fent.hash import Hash

__all__ = ["FentSet", "FentExistsMixin", "FentAssocMixin", "FentEvenMixin",
           "ProxyTrie", "sharedmem_trim_cache", "sharedmem_clear_caches"]

sharedmem_cache = defaultdict(weakref.WeakValueDictionary)
def sharedmem_trim_cache():
	"""Iterates over all objects in the caching system and removes
	   references to any unreachable objects.

	   This causes the underlying memory of unreachable objects to be
	   released and reclaimed by the operating system."""

	# Collect unreachable objects, then iterate over all cached objects
	# to see if any of the objects are now unreachable (due to a reference
	# from the weakref.WeakValueDictionary), if so delete the weakref to
	# make it reclaimed by the operating system.
	gc.collect()
	for cache in sharedmem_cache.itervalues():
		for k,tr in cache.iteritems():
			if tr
