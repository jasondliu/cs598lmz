import threading
threading.stack_size(67108864)

# Bootstrapping for python 3 compatibility
import imp
import sys
try:
    import best_effort_tracing
    imp.reload(best_effort_tracing)
    sys.modules["best_effort_tracing"] = best_effort_tracing
except ImportError:
    pass

# From the satori package
from best_effort_tracing import trace


def main():
    # Create new best_effort_tracing session
    with trace.Session('satori', '0.1') as session:
        # Create new best_effort_tracing thread
        with session.new_thread():
            time.sleep(0.1)


if __name__ == '__main__':
    main()
