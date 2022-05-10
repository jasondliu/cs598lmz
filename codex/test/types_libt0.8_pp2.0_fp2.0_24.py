import types
types.new_class('Consumer')

Types.new_class('Producer', fields=['docstring:str'])

class Consumer(object):
    """
    A Consumer of a Producer.
    """
    def accept_producer(self, producer):
        assert isinstance(producer, Producer)
        return

class Producer(object):
    """
    A Producer of values.
    """
    def get_content(self):
        raise NotImplementedError()

class ProducerConsumer(Consumer, Producer):
    """
    A Producer of Consumers.
    """
    def accept_producer(self, producer):
        assert isinstance(producer, Consumer)
        return

def accept_producer(producer):
    assert isinstance(producer, Producer)
    return

def get_content(self):
    raise NotImplementedError()

def do_str():
    return "str"

