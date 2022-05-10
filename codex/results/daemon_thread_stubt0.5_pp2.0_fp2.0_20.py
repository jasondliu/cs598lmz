import sys, threading

def run():
    while True:
        try:
            print("running...")
            time.sleep(1)
        except KeyboardInterrupt:
            print("exiting...")
            sys.exit(0)

thread = threading.Thread(target=run)
thread.start()

# do something else
</code>
This works fine, but it seems like a hack.  Is there a better way to do this?

