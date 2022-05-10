import weakref

from pyres.compat import import_module, string_types, integer_types, binary_type
from pyres.task import Task, TaskInstance
from pyres.utils import make_class_key
import pyres
import uuid

class NoQueueError(Exception): pass
class NoJobError(Exception): pass

def get_queue_from_key(key):
    if isinstance(key, string_types):
        parts = key.split(':')
        if len(parts) == 2:
            queue = parts[0]
        else:
            queue = 'default'
    else:
        queue = 'default'
    return queue

def get_queue(queue_name):
    """Get a queue by name. :attr:`queue_name` will be looked up in
    :attr:`pyres.queues`"""
    if queue_name not in pyres.queues:
        raise NoQueueError("Queue with name '%s' does not exist" % queue_name)
    return pyres.queues[queue_name]
