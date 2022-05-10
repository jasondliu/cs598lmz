import sys, threading

def run():
    while True:
        sys.stdout.write("%d\n" % (threading.active_count()-1,))
        sys.stdout.flush()
        time.sleep(1)

def main():
    threading.Thread(target=run).start()
    while True:
        print("Hello")
        time.sleep(2)

main()
</code>
When I run it, I get:
<code>$ python3 app.py 
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
