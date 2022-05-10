fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a workaround for http://bugs.jython.org/issue2422
import sys
if sys.platform == 'java':
    raise Exception('This test hangs on Jython due to a bug in the interpreter')

# This is a workaround for http://bugs.jython.org/issue2422
import sys
if sys.platform == 'java':
    raise Exception('This test hangs on Jython due to a bug in the interpreter')

# This is a workaround for http://bugs.jython.org/issue2422
import sys
if sys.platform == 'java':
    raise Exception('This test hangs on Jython due to a bug in the interpreter')

# This is a workaround for http://bugs.jython.org/issue2422
import sys
if sys.platform == 'java':
    raise Exception('This test hangs on Jython due to a bug in the interpreter')

# This is a workaround for http://bugs.jython.org/issue2422
import sys
if sys.platform == 'java':
    raise Exception('This test hangs on Jython due to a
