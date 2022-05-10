import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def wait_for_enter():
    raw_input("Press enter to continue.")

