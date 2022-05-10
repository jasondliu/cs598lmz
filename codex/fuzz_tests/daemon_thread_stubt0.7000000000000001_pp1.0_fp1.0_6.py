import sys, threading

def run():
    sys.stdout.write("Please type something: ")
    a = sys.stdin.readline()
    print("You typed %s" % a)

t = threading.Thread(target=run)
t.daemon = True
t.start()

print("Doing other things...")
sys.stdout.write("Please type something: ")
a = sys.stdin.readline()
</code>
Doesn't work as expected, it always waits for the main thread.

