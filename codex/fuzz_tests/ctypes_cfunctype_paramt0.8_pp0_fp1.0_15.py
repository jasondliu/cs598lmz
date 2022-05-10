import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte)

def create_pyfunc(code):
    class FakeModule(object):
        pass
    class FakeDictionary(object):
        pass

    # run an instruction and return the resulting accumulator
    def run(instr, acc):
        # set up dictionary for execution
        fm = FakeModule()
        fm.__dict__ = FakeDictionary()
        fm._running = 1
        fm.__name__ = '<stdin>'
        fm.code = code

        # execute the code
        fm.__dict__[instr]()

        # get the accumulator
        acc = fm.__dict__['_']

        return acc

    return FUNTYPE(run)

def main():
    # create the code to use
    code = """
# code generated with randcompile.py
import os
import random
_ = 0
def a():
    global _
    _, = random.sample(range(1000), 1)

