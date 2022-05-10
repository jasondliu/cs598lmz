import sys, threading

def run():
    while True:
        #print("thread running")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

def do_something():
    print("do something")

while True:
    try:
        do_something()
    except KeyboardInterrupt:
        print("stop")
        sys.exit(0)
</code>
When I run the above code and press Ctrl-C, I get the following message:
<code>^Cdo something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
do something
