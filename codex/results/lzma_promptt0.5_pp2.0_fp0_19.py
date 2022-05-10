import lzma
# Test LZMADecompressor
# https://stackoverflow.com/questions/29018839/compress-and-decompress-using-lzma-in-python-3-4
# https://docs.python.org/3/library/lzma.html

# https://stackoverflow.com/questions/14906764/how-to-redirect-stdout-to-both-file-and-console-with-scripting

import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

# https://stackoverflow.com/questions/1490
