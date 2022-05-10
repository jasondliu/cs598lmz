import threading
# Test threading daemon
def f1(sleep_time):
    time.sleep(sleep_time)
    print(scipy.integrate.quad(lambda x:x**2, 0, 3))
    #print(scipy.integrate.quad(lambda x:x**4, 0, 3))
    pass

def f2(sleep_time):
    time.sleep(sleep_time)
    print(scipy.integrate.quad(lambda x:x**2, 0, 3))
    #print(scipy.integrate.quad(lambda x:x**4, 0, 3))
    pass
t1 = threading.Thread(target=f1, args=(2,))
t2 = threading.Thread(target=f2, args=(3,))
t1.start()
t2.start()
# Test Multiprocessing
def f1(sleep_time):
    time.sleep(sleep_time)
    print(scipy.integrate.quad(lambda x:x**2, 0, 3))
    #print(scipy.integrate.
