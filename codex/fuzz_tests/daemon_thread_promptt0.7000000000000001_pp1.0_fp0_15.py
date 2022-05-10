import threading
# Test threading daemon
import time
import sys
import os

# Import the shared library, assuming that it is in the same directory
sys.path.append(os.path.join(os.path.dirname(__file__), '../../build/bindings/python'))

import shared_lib

# To make a python module, we need to do the following:
# * sub class the shared_lib.PyDemoModule class
# * implement the setup and teardown methods
# * implement the run method
# * implement a static method to register the module, called register_module

class DelayModule(shared_lib.PyDemoModule):
    """A simple module"""
    def __init__(self):
        shared_lib.PyDemoModule.__init__(self)
        self.delay = 0
        self.delay_lock = threading.Lock()

    @staticmethod
    def register_module(name, manager):
        """Register a module with the shared library"""
        manager.register_module(name, DelayModule)

    def setup(self):
        """Setup the module"""
        #
