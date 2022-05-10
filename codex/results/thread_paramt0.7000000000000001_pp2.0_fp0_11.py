import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Output from a thread.\n")).start()
 
# Note: the following line is now redundant, since __main__ is the default
#       target for top-level code.
if __name__ == "__main__":
    print("Output from the main thread.")

##    Output from a thread.
##    Output from the main thread.

################################################################################
# 9.5. Creating Threads Using the threading Module
# The threading module
# The threading module makes working with threads even easier. Threads can be
# created using the threading.Thread class by passing a callable object to its
# constructor. For example:
#    import threading, zipfile
#    class AsyncZip(threading.Thread):
#        def __init__(self, infile, outfile):
#            threading.Thread.__init__(self)
#            self.infile = infile
#            self.outfile = outfile
#        def run(self):
#            f = zipfile.ZipFile(self.outfile, 'w', zipfile
