import threading
# Test threading daemon

def test_func1():
    print("Hi! I'm test function1.\n")
    time.sleep(2)


def test_func2():
    print("Hi! I'm test function2.\n")
    time.sleep(3)


def main():
    t1 = threading.Thread(target=test_func1) # you must create a thread object, and pass a callable object through the target argument.
    t2 = threading.Thread(target=test_func2)
    t1.start()
    t2.start()
    t1.join() # join is for waiting for the thread to complete
    t2.join()
    print("threads completed\n")

if __name__ == "__main__":
    main()
</code>
Problem:
When I execute the code, I got the following output:
<blockquote>
<p>Hi! I'm test function2.</p>
<p>threads completed</p>
</blockquote>
The function test_func1() doesn't execute.
Question:
Why doesn
