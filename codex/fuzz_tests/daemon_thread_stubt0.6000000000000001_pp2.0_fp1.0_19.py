import sys, threading

def run():
    while True:
        print("threading")
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("main")
    sys.stdout.flush()
    time.sleep(1)
</code>
Output:
<code>main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
main
</code>
But, when I use <code>threading.Thread(target=run, daemon=True)</code>, I get the expected output:
<code>main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
threading
main
