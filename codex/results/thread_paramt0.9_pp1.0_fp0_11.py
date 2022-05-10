import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello, world\n")).start()

class Blah():
    def __init__(self):
        pass

    def print_stuff(self):
        print(" ")
        sys.stdout.write("hello, world\n")

    def thread_stuff(self):
        threading.Thread(target=lambda: sys.stdout.write("hello, world\n")).start()
