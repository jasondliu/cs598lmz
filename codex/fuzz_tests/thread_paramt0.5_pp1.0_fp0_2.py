import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

# This will print a dot every second until you interrupt the program
# (e.g. with ctrl-C).

# Note that this is just a demonstration, and you can do the same thing
# with a loop and time.sleep().
# The purpose of this example is to show that you can start threads
# that run in the background while the main thread continues on.

# If you want to see the output of the background thread, you can
# uncomment the print statements.
