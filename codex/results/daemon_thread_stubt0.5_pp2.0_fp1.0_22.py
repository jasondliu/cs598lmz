import sys, threading

def run():
    while True:
        print('Hello from thread %s' % threading.currentThread())
        sys.stdout.flush()

def run_with_limited_cpu(cpu_limit=0.5):
    def limit_cpu():
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity(range(4))

    t = threading.Thread(target=limit_cpu)
    t.start()

if __name__ == '__main__':
    run_with_limited_cpu()
    run()
</code>

