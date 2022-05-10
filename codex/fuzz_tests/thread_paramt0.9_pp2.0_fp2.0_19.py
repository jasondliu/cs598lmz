import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Welcome to Hackslash!"), args=()).start()

# Custom exception
class ArgumentFormatException(Exception):
    pass

class IllegalArgumentException(Exception):
    pass

class InvalidArgumentException(Exception):
    pass

# Globals
args = ' '
dirs = {
    'pwd': os.getcwd()
}

# Utility functions
def getAbsolutePathTo(directory):
    return os.path.abspath(directory)

def nonBlankLines(f):
    for l in f:
        line = l.rstrip()
        if line: yield line

def getDirPrompt():
    return '  ' + dirs['pwd'] + ': '

# Main function
def main():
    def takeInput():
        args = input(getDirPrompt())
        parseInput(args)
    while 1:
        try:
            takeInput()
        except Exception as e:
            print(e)

# Parse initial arguments
def parseInput(args):
    args
