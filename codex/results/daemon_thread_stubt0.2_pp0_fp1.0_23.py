import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    time.sleep(1)
</code>
I would expect the output to be:
<code>Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
</code>
But instead I get:
<code>Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello

