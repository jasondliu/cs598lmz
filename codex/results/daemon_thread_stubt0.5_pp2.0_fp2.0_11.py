import sys, threading

def run():
    print("thread {} started".format(threading.get_ident()))
    while True:
        time.sleep(1)
        print("thread {} is running".format(threading.get_ident()))

threading.Thread(target=run).start()

print("thread {} started".format(threading.get_ident()))
while True:
    time.sleep(1)
    print("thread {} is running".format(threading.get_ident()))
</code>
Output:
<code>thread 140734765944064 started
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 140734765944064 is running
thread 14
