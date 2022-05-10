import sys, threading

def run():
    while True:
        try:
            raw_input()
        except EOFError:
            print
            break

result = [False]

def service():
    while True:
        print "Service call"
        try:
            raw_input()
        except EOFError:
            result[0] = True
            break

t = threading.Thread(target=service)
t.daemon = True
t.start()

run()

print result[0]
</code>


A:

I have no idea what you are trying to achieve but EOF errors are a "control C"
<code>import sys

def run():
    for i in xrange(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

try:
    run()
except KeyboardInterrupt:
    print "Control C"
</code>
I believe the reason your code is failing is the exception is being raised in the first raw_input and is terminating the process right then. I know the shell is not displaying the
