import sys, threading

def run():
    x = 0
    while True:
        x += 1
    print(x)

for i in range(10):
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

# wait for all threads to terminate
#while threading.activeCount() != 1:
#    pass

print('finished')
