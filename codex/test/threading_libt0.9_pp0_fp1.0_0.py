import threading
threading.current_thread().setName("Main Thread")
print(threading.current_thread().getName())


def square(numbers):
    print(threading.current_thread().getName() + " is executing this function")
    for i in numbers:
        time.sleep(0.2)
        print("Square: " , i * i)


def cube(numbers):
    print(threading.current_thread().getName() + " is executing this function")
    for i in numbers:
        time.sleep(0.2)
        print("Cube: ", i * i * i)


numbers = [2, 4, 7, 9]

t1 = time.time()
square(numbers)
cube(numbers)
print("Done in: ", time.time() - t1)
print("Bye")
