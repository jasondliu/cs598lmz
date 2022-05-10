import threading
# Test threading daemon
import colorama
import logging
# Test logging
import logging.handlers
# Test log handler
import subprocess
# Test subprocess
import signal
# Test signal
import queue
# Test priority queue
import time
import multiprocessing
# Test multi threading

# Test global vars
testGlobalVar = 1

# Test class
class TestClass:
    # Test global var
    testGlobalVar = 1
    def __init__(self):
        # Test non global var
        self.testVar = 1
        # Test global var
        global testGlobalVar
        print(testGlobalVar)
    
    def testFunction(self):
        # Test non global var
        print(self.testVar)
        # Test global var
        global testGlobalVar
        print(testGlobalVar)

# Test functions
def testFunction():
    # Test global var
    global testGlobalVar
    print(testGlobalVar)
    
    # Test list
    testList = list()
    testList.append(1)
    print(testList)
    
    # Test dict
   
