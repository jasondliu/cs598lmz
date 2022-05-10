import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello world")).start()

# will output "hello world" in python-mode
