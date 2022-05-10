import types
types.MethodType(container.containerProducer, container_type)

container_type
container_type.containerProducer()
 
Getting information on objects
print(container_type.containerProducer)
help(container_type.containerProducer)
container_type.containerProducer.__doc__
container_type.containerProducer.__name__
container_type.containerProducer.__module__

The metaClass approach

class MyClass:
    __metaclass__=MyMetaClass

but there isnt a standard across
python 2
python 3

so we use ABC
from abc import ABCMeta, abstractmethod

class MyClass(object)
    __metaclass__=ABCMeta
        
 

Inheritance

from abc import ABCMeta, abstractmethod

class TransportContainer(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def containerProducer(self):
        """
        Returns the string name of the object that produced
        this container.
        """
        
from shipping import TransportContainer
from abc import ABCMeta,
