import sys, threading

def run():
    sys.stdout.write("finished")
    sys.stdout.flush()
# threading.Thread(target=run).start()

import coverage

import pytest
