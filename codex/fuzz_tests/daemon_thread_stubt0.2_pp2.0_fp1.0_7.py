import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("World")
    time.sleep(1)
</code>
The output is:
<code>World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
Hello
