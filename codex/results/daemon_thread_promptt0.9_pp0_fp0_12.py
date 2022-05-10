import threading
# Test threading daemon thread
def thr_func(num):
	global thr
	print(len(thr))
	print(num)
#	print(thr[num].is_alive())

def mainLoop():
    global thr
    thr = []
    for i in range(2):
        thr.append(threading.Thread(target=thr_func, args=(i,),daemon=True))
    for t in thr:
        t.setDaemon(True)
        t.start()
#        t.join()
        print(t.is_alive())
    print("Work done")
    for t in thr:
        print(t.is_alive())
            
if __name__ == '__main__':
    mainLoop()
    try:
        while True:
            time.sleep(1)
            print("Main run")
    finally:
        print("Exit main")
