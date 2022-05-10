import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Uses a thread to read input while the main thread continues doing other work.
def readInput(callback):
    def wrappedInput():
        callback(input())
    threading.Thread(target=wrappedInput).start()

# Now you can do things like:
readInput(print)

# to have input() run in another thread.
#
# The callback will be called with the user's input as a parameter.
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.
