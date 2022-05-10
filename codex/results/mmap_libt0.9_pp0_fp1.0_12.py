import mmapi
import mmcommands
import os
import threading
import time

from common import mmApp


def abort_timeout(fn,args=[],timeout=3):
    """Purpose of this function is to enforce a time out on a function call
    Currently it just spawns a thread that runs a function, returns true if
    the thread is running after the timeout and returns false if the thread
    has ended before the timeout

    fn is the function you want to wrap to enforce a timeout on.
    args is a list of arguments you want to pass to fn.
    timeout is the tiumeout in seconds that you want to wait before assuming
    the function failed
    """

    #create thread object
    t = mmcommands.MThread(target=fn,args=args)
    t.setDaemon(True)
    t.start()

    #wait for thread to die or timeout
    t.join(timeout)
    # return false if the thread is still running
    if t.isAlive():
        print "abort_timeout: Tired of waiting, assuming error"
        # stop the thread by throwing
