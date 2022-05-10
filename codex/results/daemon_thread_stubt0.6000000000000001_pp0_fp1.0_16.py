import sys, threading

def run():
    cmd = 'python ' + sys.argv[1]
    os.system(cmd)

thread = threading.Thread(target=run)
thread.start()

while True:
    try:
        print 'running'
        time.sleep(1)
    except KeyboardInterrupt:
        print 'stopping'
        os.system('pkill -f ' + sys.argv[1])
        sys.exit(0)
</code>

