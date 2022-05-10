import sys, threading

def run():
    for i in range(10):
        print(i, threading.main_thread(), threading.active_count())
        time.sleep(0.5)

if __name__ == "__main__":        
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
</code>
The output is the following:
<code>$ ./test.py 
0 &lt;_MainThread(MainThread, started 140565492155712)&gt; 4
1 &lt;_MainThread(MainThread, started 140565492155712)&gt; 4
2 &lt;_MainThread(MainThread, started 140565492155712)&gt; 4
3 &lt;_MainThread(MainThread, started 140565492155712)&gt; 4
4 &lt;_MainThread(MainThread, started 140565492155712)&gt; 4
0 &lt;Thread(Thread-1, started 14056549
