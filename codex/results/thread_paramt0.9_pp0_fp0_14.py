import sys, threading
threading.Thread(target=lambda:sys.stdout.write("thread mini a b c ; hijklmstuvwxyz\n"), daemon=True).start()

sys.exit(0)





interface=1

if interface==0:
    #import thread,time
    import sys,threading
    #create worker thread
    thread=threading.Thread(target=threadLoop)
    thread.start()
    #time.sleep(3)
    str=""
    for c in range(0,26):
        for k in sys.stdin:
            if k=="":
                break
            str+=k
            if k=="\n":
                break
        #print "The thread got", str
        str.upper()
        thread.join()
        sys.stdout.write(str)
        str=""
        thread=threading.Thread(target=threadLoop)
        thread.start()

if interface==1:
    #p=Popen(cmd, shell=True, bufsize=1, stdin=PIPE, stdout=PIPE)
    p=P
