import threading
# Test threading daemon in python
# http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/

class TestHU(unittest.TestCase):

    def test_something(self):

	    from io import StringIO
	    import sys
	    from hu_utils import ctx

	    # Capture output
	    orig_stdout = sys.stdout
	    orig_stderr = sys.stderr
	    sys.stdout = mystdout = StringIO()
	    sys.stderr = mystderr = StringIO()

	    ctx()
	    # note that there must be no output to stdout or stderr to execute 'ctx()'

	    # sys.stdout = orig_stdout
	    # sys.stderr = orig_stdout

	    output_stdout = mystdout.getvalue().strip()
	    output_stderr = mystderr.getvalue().strip()

	    print('test_something
