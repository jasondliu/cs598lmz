import sys, threading

def run():
    while True:
        print "Hello"

thread = threading.Thread(target=run)
thread.start()

while True:
    print "Goodbye"
</code>
This is the output:
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
Good
