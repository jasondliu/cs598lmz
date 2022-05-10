import select
# Test select.select

import threading
import Queue
import time

inq = Queue.Queue()
outq = Queue.Queue()

