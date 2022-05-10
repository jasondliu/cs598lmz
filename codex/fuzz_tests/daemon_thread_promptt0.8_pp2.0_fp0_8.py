import threading
# Test threading daemon


def first():
    print('Trigger first')


def second():
    print('Trigger second')


def third():
    print('Trigger third')


def fourth():
    print('Trigger fourth')


def fifth():
    print('Trigger fifth')


# Create threads
threads = []
t = threading.Thread(target=first)
t.setDaemon(True)
threads.append(t)

t = threading.Thread(target=second)
t.setDaemon(True)
threads.append(t)

t = threading.Thread(target=third)
t.setDaemon(True)
threads.append(t)

t = threading.Thread(target=fourth)
t.setDaemon(True)
threads.append(t)

t = threading.Thread(target=fifth)
t.setDaemon(True)
threads.append(t)

# Start threads
for t in threads:
    t.start()

# Wait for threads
for t in threads:
    t.join()


