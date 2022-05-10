import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Sys.stdout\n')).start()
threading.Thread(target=lambda: sys.stderr.write('Hello from Sys.stderr\n')).start()

msg = """
Warning: 
This version of Python has problems with -X options 
such as -X, -X futurize, and -X paste, and is not fully supported. 
Run Python 2.7 instead.
"""

sys.stdout.write(msg)
sys.stderr.write(msg)

def printer(delay, msg):
    while True:
        time.sleep(delay)
        print(msg)

threading.Thread(target=printer, args=(1, 'spam')).start()
