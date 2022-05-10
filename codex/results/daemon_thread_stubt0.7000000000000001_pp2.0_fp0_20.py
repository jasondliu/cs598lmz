import sys, threading

def run():
    print('running...')
    sys.exit()

t = threading.Thread(target=run)
t.start()

print('runing...')
print(t.is_alive())
t.join()
print('join finished')
print(t.is_alive())

# runing...
# True
# running...
# join finished
# False
