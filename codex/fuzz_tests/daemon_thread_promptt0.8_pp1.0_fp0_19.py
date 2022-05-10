import threading
# Test threading daemon

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


def search_prime():
    global found
    print threading.currentThread().getName(), 'Searching...'
    
    for num in range(1,100):
        if is_prime(num):
            print threading.currentThread().getName(), 'Found:' , num
            found.add(num)
            #print found
            
t1 = threading.Thread(target=search_prime, args=())
t1.setDaemon(True) # Kill thread when main thread dies
t1.start()

t2 = threading.Thread(target=search_prime, args=())
t2.setDaemon(True) # Kill thread when main thread dies
t2.start()

# Sleep for a
