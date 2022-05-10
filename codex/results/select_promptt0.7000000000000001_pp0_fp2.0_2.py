import select
# Test select.select()

READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

# Our own events
NONE = 0x0000
EXCEPTION = 0x0001

# Event map
_EVENT_MAP = {}

def _create_event_map():
    for key, value in vars(select).items():
        if key.startswith('POLL'):
            _EVENT_MAP[value] = key

_create_event_map()

print(_EVENT_MAP)


def events_to_str(fd, events):
    '''
    Convert the events to strings
    '''
    result = []
    for i in _EVENT_MAP:
        if i & events:
            result.append(_EVENT_MAP[i])
    return '|'.join(result)

class Poller(object):
    '''
    Wrap select.poll() interface
    '''
    def __init__
