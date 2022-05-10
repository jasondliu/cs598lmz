import threading
# Test threading daemon

def my_func(name):
    print('Hello ' + name)
    time.sleep(3)
    print('Bye ' + name)

if __name__ == '__main__':
    t = threading.Thread(target=my_func, args=('Alice',))
    t.daemon = True
    t.start()
    print('End')

# End
# Hello Alice
# Bye Alice

# Test threading daemon

def my_func(name):
    print('Hello ' + name)
    time.sleep(3)
    print('Bye ' + name)

if __name__ == '__main__':
    t = threading.Thread(target=my_func, args=('Alice',))
    t.daemon = True
    t.start()
    time.sleep(1)
    print('End')

# End
# Hello Alice
# Bye Alice

# Test threading daemon

def my_func(name):
    print('Hello ' + name)
    time.sleep(3)
    print('Bye
