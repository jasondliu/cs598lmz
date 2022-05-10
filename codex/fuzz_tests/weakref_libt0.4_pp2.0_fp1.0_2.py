import weakref
import logging

logger = logging.getLogger(__name__)

class Message(object):
    """
    A message is a dictionary that contains a type and a message.
    """
    def __init__(self, type, message):
        self.type = type
        self.message = message

    def __str__(self):
        return str(self.__dict__)


class MessageQueue(object):
    """
    A message queue is a queue of messages.
    """
    def __init__(self):
        self.queue = Queue.Queue()
        self.handlers = []

    def put(self, message):
        """
        Put a message in the queue.
        """
        self.queue.put(message)

    def get(self):
        """
        Get a message from the queue.
        """
        return self.queue.get()

    def register(self, handler):
        """
        Register a handler.
        """
        self.handlers.append(handler)

    def unregister(self, handler):
       
