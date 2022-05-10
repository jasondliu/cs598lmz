import sys, threading

def run():
    x = raw_input("$ ")
    print "got input: " + str(x)

t = threading.Thread(target=run)
t.start()

while True:
    pass
</code>

