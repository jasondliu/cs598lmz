import sys, threading

def run():
    sys.stdout.write("%s\n" % sys.argv[1])
    sys.stdout.flush()

threading.Thread(target=run).start()

from time import sleep
sleep(1)

sys.stdout.write("%s\n" % sys.argv[2])
sys.stdout.flush()
</code>
This will work, but it's not something you should do in production. 

