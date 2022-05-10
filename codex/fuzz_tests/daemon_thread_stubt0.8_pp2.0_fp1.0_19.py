import sys, threading

def run():
    while True:
        print( "hello")
        time.sleep(1)

t1 = threading.Thread(target=run)
t1.start()
time.sleep(5)
print( "sys exit")
sys.exit()
