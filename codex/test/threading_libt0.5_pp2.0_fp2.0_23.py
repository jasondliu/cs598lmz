import threading
threading.stack_size(67108864)

def print_cube(num):
    print("Cube: {}".format(num * num * num))

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # Will execute both in parallel
    t1.start()
    t2.start()

    # Joins threads back to the parent process, which is this
    # program
    t1.join()
    t2.join()

    print("Done!")

# Two threads, one runs print_square, the other print_cube.
# Both run in parallel.
# The parent process will wait for both threads to complete
# before exiting.
