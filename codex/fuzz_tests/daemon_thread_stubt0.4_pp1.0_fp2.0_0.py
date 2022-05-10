import sys, threading

def run():
    while True:
        print "Hello"
        time.sleep(0.5)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    while True:
        print "Goodbye"
        time.sleep(0.5)
</code>
This prints:
<code>Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
Hello
