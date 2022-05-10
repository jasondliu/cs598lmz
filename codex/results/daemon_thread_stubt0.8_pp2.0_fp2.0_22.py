import sys, threading

def run():
    ex = __import__(sys.argv[1]).main()
    print "DONE RUN",ex

t = threading.Thread(target=run)
t.start()
