import sys, threading

def run():
    print("Thread {} started".format(threading.get_ident()))
    while True:
        pass

thread_count = int(sys.argv[1])
for i in range(thread_count):
    threading.Thread(target=run).start()

print("{} threads started".format(thread_count))
