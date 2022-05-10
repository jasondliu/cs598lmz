import gc, weakref, os
import pymemcache.client.base

from . import conf
from . import binpacking
from . import util, hashing
from .item import Item
from .debug import Debug

class Cache(object):
   def __init__(self, binpacking_method, memcache_hosts):
      self._memcache_hosts = memcache_hosts
      self._memcache_client = pymemcache.client.base.Client(self._memcache_hosts, pickleProtocol=2, connect_timeout=2)
      self._binpacking_method = binpacking.binpacking_method_map[binpacking_method]
      self._first_bin = True
      self._bin = None
   def save(self, item):
      if self._first_bin:
         self._bin = self._binpacking_method()
         self._first_bin = False
      saved_data = item.save(self._bin)
      #print("Saved %s as '%s' using %d MB, %d memcache keys" % (item.absolute_entry_path,
