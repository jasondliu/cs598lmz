import lzma
lzma.open
import pyinotify
import os
from multiprocessing.dummy import Pool as ThreadPool

#inotify wrapper
class Inotify(pyinotify.ProcessEvent):
    def __init__(self,callback=None,names=[]):
        self._wm = pyinotify.WatchManager()
        self._callback = callback
        flags = pyinotify.ALL_EVENTS
        self._notifier = pyinotify.Notifier(self._wm,self)
        self._mask = flags
        self.names = names
        threads = 6
        self.pool = ThreadPool(threads)
    def add_watch(self,directory):
        self._wm.add_watch(directory,self._mask,self)
    
    def process_IN_CREATE(self,event):
        #print("Creating:", event.pathname)
        if event.pathname in self.names:
            self.pool.apply_async(self._wrap_pathname,args=[event.pathname])
    def _wrap_pathname(self
