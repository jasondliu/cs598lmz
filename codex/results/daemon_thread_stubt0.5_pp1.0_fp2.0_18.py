import sys, threading

def run():
    while True:
        print("Hello world")
        time.sleep(0.5)

def main():
    t = threading.Thread(target=run)
    t.start()

    while True:
        print("Goodbye world")
        time.sleep(0.5)

main()
</code>
The output is:
<code>Hello world
Goodbye world
Hello world
Goodbye world
Hello world
Goodbye world
Hello world
Goodbye world
...
</code>

