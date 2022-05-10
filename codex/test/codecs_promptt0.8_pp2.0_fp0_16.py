import codecs
# Test codecs.register_error()

import sys
# reset sys.stderr and sys.stdout to solid files
sys.stderr = open(r'test_stderr', 'w')
sys.stdout = open(r'test_stdout', 'w')

