import threading
threading.stack_size(67108864)

start = time.time()

def do_something():
    print("Sleeping now")
    time.sleep(5)
    print("Done sleeping")
    return 5

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.time()

print(f'Finished in {round(finish-start,2)} seconds(s)')

# print("Hello")
#
# def print_hello():
#     print("Hello")
#
# t1 = threading.Thread(target=print_hello)
# t2 = threading.Thread(target=print_hello)
#
# t1.start()
# t2.start()
#
# print("Done")
#
# t1.join()
# t2.join()
#
# finish = time.time()
#
# print
