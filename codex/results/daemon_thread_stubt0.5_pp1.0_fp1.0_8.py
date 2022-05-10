import sys, threading

def run():
    t = threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n"))
    t.start()
    t.join()

run()
