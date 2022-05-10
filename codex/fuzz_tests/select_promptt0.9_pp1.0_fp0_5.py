import select
# Test select.select on a event object that has a notify() and get_fileno()
# method.

class TestEvent:

    def __init__(self):
        self.read_fds = []

    def notify(self):
        self.read_fds.append(1)

    def get_fileno(self):
        return -1

event = TestEvent()
event.select = select.select

t = Thread(target=event.notify)
t.start()
tim
