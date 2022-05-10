import select
import platform

def os_specific_sleep():
    if platform.system() == "Linux":
        select.select([], [], [], 0.1)

if __name__ == "__main__":
    import thread

    def foo(n):
        while n:
            print('hello')
            n -= 1
            os_specific_sleep()

    def bar(n):
        while n:
            print('goodbye')
            n -= 1
            os_specific_sleep()

    thread.start_new_thread(foo, (10,))
    thread.start_new_thread(bar, (20,))

    # main thread waits for all sub threads to finish
    while threading.activeCount() > 1:
        os_specific_sleep()
    else:
        print("all threads finished!")
