import sys, threading

def run():
    t = threading.current_thread()
    print t.name
    for i in range(1, 10):
        if i == 5:
            t.join()
        sys.stdout.write('%s\n' % i)

def main():
    for i in range(4):
        threading.Thread(target=run, name='thread %s' % i).start()

if __name__ == '__main__':
    main()
    #run()
