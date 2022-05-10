import sys, threading

def run():
    print "in run function"
    print "sys.stdin:",sys.stdin
    print "sys.stdout:",sys.stdout
    while True:
        print "in while"
        #print "1. sys.stdin:",sys.stdin
        #print "2. sys.stdout:",sys.stdout
        commandline = sys.stdin.readline()        # Read raw user input
        print "commandline:", commandline
        print "3. sys.stdin:",sys.stdin
        #sys.stdout.write( '3. Hello, World.\n')
        #sys.stdout.flush()

def start():
    thread = threading.Thread(target=run)
    thread.daemon = True

    print "in start"
    print "sys.stdin:",sys.stdin
    print "sys.stdout:",sys.stdout
    sys.stdout.write( '1. Hello, World.\n')
    sys.stdout.flush()
    thread.start()
    return thread
