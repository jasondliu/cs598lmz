import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

# DEBUGGING
import pdb; pdb.set_trace()
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')
# logging.warning('This is a warning.')
# logging.critical('This is critical.')
# logging.error('This is an error.')
# logging.info('This is an info.')
# logging.basicConfig(filename='myProgram.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# RE
import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo = phone_num_regex
