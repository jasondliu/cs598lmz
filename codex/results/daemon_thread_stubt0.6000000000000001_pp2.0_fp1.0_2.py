import sys, threading

def run():
    global idx
    while(True):
        if(idx == len(target)):
            break
        if(target[idx] == '1'):
            print("#", end = "")
        else:
            print(" ", end = "")
        idx += 1
    print()

target = sys.argv[1]
idx = 0

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
t3 = threading.Thread(target=run)
t4 = threading.Thread(target=run)
t5 = threading.Thread(target=run)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
