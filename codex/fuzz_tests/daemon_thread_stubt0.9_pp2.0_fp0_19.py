import sys, threading

def run():
   print "Running"

thread = threading.Thread(target=run)
thread.start()
