import sys, threading

def run():
    file = open('/proc/sys/vm/drop_caches')
    file.write('3')
    file.close()

if __name__ == '__main__':
    for i in range(0, 100):
        threading.Thread(target=run).start()
    print "done"
</code>

