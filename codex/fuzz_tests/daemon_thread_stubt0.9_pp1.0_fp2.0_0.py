import sys, threading

def run():
    while(True):
        time.sleep(1)

if __name__=='__main__':
    if len(sys.argv)<3:
        print 'Usage: ./main.py <appName> <numPhysical> <numVirtual>'
        exit()

    app = sys.argv[1]
    numPhysical = int(sys.argv[2])
    numVirtual = int(sys.argv[3])
    os.system('./'+app+' '+str(numPhysical)+' '+str(numVirtual))
    numPhysical = len(sys.argv)-3
    threads = []

    for x in range(0, numPhysical):
        threads.append(threading.Thread(target=run))

    for x in range(0, numPhysical):
        threads[x].start()

    for x in range(0, numPhysical):
        threads[x].join()

    time.sleep(1)
    os.system('killall '+app);
    time.sleep(1)
