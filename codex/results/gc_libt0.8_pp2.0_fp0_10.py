import gc, weakref, sys

from vtrace.tests.helpers import getTrace

def resolveSymbol(trace, symstr, lib=None):
    "Resolve a symbol in the process"
    if lib == None:
        lib = trace.getMeta("LibraryBases")[0]
    return trace.getSymByName(symstr, lib)

class TestTrace:

    def test_forcebreak(self):
        trace = getTrace()
        bpid = trace.breakpoints.add(0x0, trace.BREAK_CODE)
        trace.run()
        assert bpid in trace.getBreakpointHits()

    def test_libload(self):
        trace = getTrace()
        trace.requireNotRunning()
        trace.run()
        trace.requireRunning()
        libs = trace.getMeta("LibraryBases")
        assert len(libs) > 0
        trace.requireNotRunning()

    def test_callbacks(self):

        trace = getTrace()

        class MyCallback:

            def __init__(self):

