import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Goodbye World")
    time.sleep(1)
</code>
The output is:
<code>Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye World
Hello World
Goodbye
