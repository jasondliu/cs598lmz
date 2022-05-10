import sys, threading

def run():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6

    #print("starting thread ")
    n = 0
    while n == 0:
        if not q1.empty():
            print("coming in thread")
            aggval = q1.get()
            q2.put(True)
            print("enqueue")
            #break
            #sys.exit()
            #print(aggval)
        if not q3.empty():
            print("commig in thread 2")
            aggval = q3.get()
            q4.put(True)
            #break
            #print(aggval)
            #sys.exit()
        if not q5.empty():
            print("commig in thread 3")
            aggval = q5.get()
            q6.put(True)
            #break
            #print(aggval)
            #sys.exit()
        #print("if coming here")
        time.sleep(1)

threading.Thread(target=run).start
