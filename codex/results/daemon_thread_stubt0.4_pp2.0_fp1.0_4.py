import sys, threading

def run():
    while True:
        sys.stdout.write("\r" + "*" * i)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * i)
        sys.stdout.flush()
        time.sleep(0.3)

t = threading.Thread(target=run)
t.start()

for i in range(100):
    time.sleep(1)
    print("\r" + "=" * i, end="")

sys.stdout.write("\n")
sys.stdout.flush()
</code>
The problem is that the output is not correct. It looks like this:
<code>============================================================
                                                            *
                                                            *   
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                            *
                                                           
