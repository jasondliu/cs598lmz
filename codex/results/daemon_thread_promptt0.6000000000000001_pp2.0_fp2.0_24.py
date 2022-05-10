import threading
# Test threading daemon

def run():
    print('Start Thread')
    time.sleep(5)
    print('End of Thread')

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print('Main Thread')
    time.sleep(0.5)

print('End of Main')

# Test process
def run():
    print('Start Process')
    time.sleep(5)
    print('End of Process')

p = multiprocessing.Process(target=run)
p.start()

while True:
    print('Main Process')
    time.sleep(0.5)

print('End of Main')

# Test threading
def run():
    print('Start Thread')
    time.sleep(5)
    print('End of Thread')

t = threading.Thread(target=run)
t.start()

while True:
    print('Main Thread')
    time.sleep(0.5)

print('End of Main')
 
# Test threading
def run
