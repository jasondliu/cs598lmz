import sys, threading

def run():
    while True:
        print "hello world"
        time.sleep(.5)


t = threading.Thread(target=run)
t.start()

input()
print "abc"
input()
