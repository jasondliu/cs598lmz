import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Output:
# Hello World

# Reference: https://stackoverflow.com/questions/247770/retrieving-stdout-from-a-script-called-using-shel
