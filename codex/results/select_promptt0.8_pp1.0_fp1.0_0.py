import select
# Test select.select function
# See http://stackoverflow.com/questions/1365215/on-windows-how-to-make-select-not-hang

def is_readable(f):
    # this is a workaround for select.select, which doesn't seem to be implemented in Windows properly
    # (it works on Linux)
    # this may not work for all cases, in which case we need to rewrite our code to use select.poll
    # or use the new selectors module in python 3.5+
    return True

_previousReadables = []

def test_select():
    readables, _, _ = select.select(_previousReadables, [], [])

def test_main(file_name):
    with open(file_name, "r") as f:
        test_select()
        _previousReadables.append(f)

if __name__ == "__main__":
    test_main(sys.argv[1])
</code>
To run the script on the command line, I just type the following
<code>python socket_test.py
