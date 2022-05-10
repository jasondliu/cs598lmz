import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

t = threading.Thread(target=run)
t.start()

# ---------------------------------------------------------------
# $ python3 threading_simple.py

# Hello from thread <Thread(Thread-1, started 123145304048640)>

# $ python3 threading_simple.py

# Hello from thread <Thread(Thread-1, started 123145304048640)>

# $ python3 threading_simple.py

# Hello from thread <Thread(Thread-1, started 123145304048640)>
# ---------------------------------------------------------------
