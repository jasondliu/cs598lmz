import types
types.NoneType

import types
types.FunctionType

isinstance(None, types.NoneType)

import types
types.ClassType

isinstance(object, types.ClassType)
isinstance(None, types.ClassType)

import types
types.InstanceType

isinstance(story, types.InstanceType)


# This module matches the ones in Chapter 6, so it has
# a main function used for testing.

def test_dog_tricks(dog_name):
    """
    Make sure the dog can do everything it should be able to.
    """
    dog = Dog(dog_name)
    print("The dog's name is", dog.name)
    dog.bark()
