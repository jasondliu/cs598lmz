import signal
# Test signal.setitimer() is defined when it should be.
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

import threading
# The OS-specific threading module may define some thread-local objects
# that must be initialized after each fork().  This makes threading work
# correctly after fork().
threading._after_fork()


def main():
    if sys.stdin.isatty():
        import idlelib.pyshell
    else:
        try:
            import runpy
        except ImportError:
            pass
        else:
            runpy._run_module_as_main()
        del sys.argv[0]
        sys.path.insert(0, '')
        import runpy

        runpy.run_module('__main__', run_name='__main__', alter_sys=True)

if __name__ == '__main__':
    main()
