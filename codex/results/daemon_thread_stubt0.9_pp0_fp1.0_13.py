import sys, threading

def run():
    return b''.join(sys.stdin.buffer.readlines())

stdout_lock = threading.Lock()
sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer), line_buffering=True)
with stdout_lock:
    print(run())
