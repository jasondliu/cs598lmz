import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()

import logging, logging.handlers
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s.%(msecs)-3d:%(levelname)s:%(name)s:%(message)s',
    datefmt='%H:%M:%S')

#logger = logging.getLogger('main')
#logger.setLevel(logging.DEBUG)
#formatter = logging.Formatter('%(asctime)s.%(msecs)-3d:%(levelname)s:%(name)s:%(message)s','%H:%M:%S')
#handler = logging.handlers.RotatingFileHandler('/tmp/logger.log',maxBytes=100000,backupCount=2)
#handler.setFormatter(formatter)
#logger.addHandler(handler)

#logger = logging.getLogger('main')
#logger.setLevel(logging.DEBUG)
