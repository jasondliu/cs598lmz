import threading
# Test threading daemon
import time
import traceback

def thread_function(name):
    while True:
        print(f"Thread {name}: running")

def test_test_test():
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    x.start()
    time.sleep(3)
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())


def raise_excpetion(i):
    raise Exception(f"Error : {i}")

def thread_function_exception(name):
    print(f"Thread {name}: running")
    raise_excpetion('a')


def test_thread_error():
    x = threading.Thread(target=thread_function_exception, args=(1,))
    x.start()
    x.join()
    print(f"{x.is_alive()}")


def skip_condition(number):
    print(f"Skip condition : number = {number}")

