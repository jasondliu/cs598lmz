import select
# Test select.select() for reading only
sys.stdin, out, err = select.select([sys.stdin], [], [], 10)
# sys.stdin, out, err = select.select([sys.stdin], [], [], 60)

if sys.stdin in out:
    print('Found input!')
</code>
The code above works fine, but if I change the timeout value to 60 (or any other larger number), select fails to find any input on stdin. Does anyone know why?


A:

This is probably because your loop's run time is less than the select timeout.
I suspect you're running a short-running loop, and are expecting <code>select</code> to return immediately when any input is available.  It doesn't work that way.
<code>select</code> will wait until the timeout has expired, then return current input file descriptors.  Therefore, if your loop is running for less than the timeout, <code>select</code> will not see any input in the interval it checked.

