import sys, threading

def run():
    sys.stdout.write("running\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("done\n")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

sys.stdout.write("waiting\n")
sys.stdout.flush()
thread.join()

sys.stdout.write("exit\n")
sys.stdout.flush()
</code>
The output is:
<code>waiting
running
done
exit
</code>

