import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# user interface
from core import pycmd

# start mongodb with the config file
print 'start the mongo_thread'
from core import db
db_thread = db.save_thread()
db_thread.setDaemon(True)
db_thread.start()

print 'start the pycmd_thread'
pycmd_thread = pycmd.start_pycmd()
pycmd_thread.setDaemon(True)
pycmd_thread.start()
