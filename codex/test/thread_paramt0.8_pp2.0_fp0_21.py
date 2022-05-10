import sys, threading
threading.Thread(target=lambda: sys.stdout.write("" + "\n")).start()

"""
https://discuss.leetcode.com/topic/81271/python-solution-similar-to-web-one-thread-for-each-test-case-using-threading-module/2

An example implementation.

This implementation will spawn a new thread for each test case.
"""

from time import sleep
import sys, threading

class StandardTestCaseRunner(object):
    def __init__(self):
        self.input = []
        self.output = []
    def parseInput(self):
        pass
    def compute(self):
        pass
    def result(self):
        return self.output

class Solution(object):
    def __init__(self):
        self.input = []
        self.output = []
    def parseInput(self):
        while True:
            try:
                self.input.append(int(raw_input()))
            except:
                break
