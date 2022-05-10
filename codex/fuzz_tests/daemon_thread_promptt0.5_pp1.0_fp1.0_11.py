import threading
# Test threading daemon

def run():
    print "Thread started"
    while True:
        print "Thread running"
        time.sleep(1)

def main():
    print "Main started"
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        print "Main running"
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
Output:
<code>Main started
Thread started
Main running
Thread running
Main running
Thread running
</code>

