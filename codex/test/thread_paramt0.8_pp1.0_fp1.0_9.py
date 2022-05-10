import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Sub\n")).start()

print("Main")

# Output:
Sub
Main
