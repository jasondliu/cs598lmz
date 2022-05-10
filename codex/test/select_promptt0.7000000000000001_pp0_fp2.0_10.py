import select
# Test select.select behavior
select.select([], [], [], 3.2)
select.select([], [], [], -1)

import threading

# Test threading.local behavior
class TestLocal(threading.local):
    def __init__(self, **kw):
        self.__dict__.update(kw)

local = TestLocal(x=1, y=2)
local.x

# Test threading.Condition behavior
condition = threading.Condition()
condition.wait(1)
condition.wait(None)
condition.wait(-1)

# Test threading.Thread behavior
def f():
    pass
thread = threading.Thread(target=f)
thread.start()
thread.join(1)
thread.join(None)
thread.join(-1)

# Test threading.Timer behavior
timer = threading.Timer(1, f)
timer.start()
timer.cancel()

timer = threading.Timer(None, f)
timer.start()
timer.cancel()

