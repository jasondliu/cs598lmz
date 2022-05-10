import sys, threading
threading.Thread(target=lambda: sys.exit(" ")).start()
while threading.active_count() != 1:
    pass

#TODO replace this with an exit status
print("done")
