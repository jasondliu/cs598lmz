import threading
# Test threading daemon
#
# This is useful for starting multiple processes that are designed to run
# indefinitely (i.e. the processes will never finish).
#
# To use, instantiate the class and then call the start() method.
#
# @author Daniel Duke <daniel.duke@monash.edu>
# @copyright (c) 2018 LTRAC
# @license GPL-3.0+
# @version 1.0.4
# @note This code is experimental
#
class daemon(threading.Thread):
    def __init__(self, name, func, args=(), kwargs={}):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.daemon = True
        
    def run(self):
        self.func(*self.args, **self.kwargs)
