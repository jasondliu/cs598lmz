import sys, threading
threading.Thread(target=lambda: sys.stdout.write("bar\n")).start()

foo = 0


def foo_func():
    global foo
    foo = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

threading.Thread(target=foo_func).start()

print("foo", foo) # Still prints 0 because thread hasn't completed.
