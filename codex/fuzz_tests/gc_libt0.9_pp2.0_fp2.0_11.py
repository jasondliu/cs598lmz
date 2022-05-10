import gc, weakref
import threading
import subprocess

class stopThreadState:
    def __init__(self, thread=None, weakref_object=None, only_when_weakref_object_alive=True):
        self.stopFlag = False
        
        if thread:
            self.thread = thread
            self.weakref_object = weakref_object
            self.only_when_weakref_object_alive = only_when_weakref_object_alive
        else:
            self.thread = None
            self.weakref_object = self
            self.only_when_weakref_object_alive = True
            
    def get_stopFlag(self):
        if self.thread:
            alive = self.weakref_object is not None if self.only_when_weakref_object_alive else True
            stopFlag = alive and self.stopFlag
        else:
            stopFlag = self.stopFlag
        
        return stopFlag
    
    def set_stopFlag(self, value):
        self.stopFlag = value
        
    def
