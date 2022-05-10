import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World")).start()

print("while loop")
while threading.active_count() != 1:
    pass



print("end")
