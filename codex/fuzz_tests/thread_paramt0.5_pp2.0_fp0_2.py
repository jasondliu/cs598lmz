import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello from thread\n")).start()
print("Hello from main")

# threading.Thread(target=lambda:sys.stdout.write("Hello from thread\n")).start()
# print("Hello from main")

# threading.Thread(target=lambda:sys.stdout.write("Hello from thread\n")).start()
# print("Hello from main")
