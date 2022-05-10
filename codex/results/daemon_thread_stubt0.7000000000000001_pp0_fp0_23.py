import sys, threading

def run():
    try:
        import asyncio
        asyncio.set_event_loop(asyncio.new_event_loop())
        from twisted.internet import asyncioreactor
        asyncioreactor.install(asyncio.get_event_loop())
    except ImportError:
        import twisted.internet.reactor
        twisted.internet.reactor.run(installSignalHandlers=0)


def daemonize():
    """
    """
    try:
        pid = os.fork()
        if pid > 0:
            # exit first parent
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/")
    os.setsid()
    os.umask(0)

    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.
