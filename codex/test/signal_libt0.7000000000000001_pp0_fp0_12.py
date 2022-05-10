import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def abort(signum, frame):
    raise IOError("Pipe closed")
signal.signal(signal.SIGPIPE, abort)

for msg in sys.stdin:
    msg = msg.strip()
    m = re.match(r"^(\d+)\s+(\d+)\s+(.*)$", msg)
