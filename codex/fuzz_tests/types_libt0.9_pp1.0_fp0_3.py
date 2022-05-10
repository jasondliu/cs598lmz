import types
types.new_class('Person')

class MartialArt(object):
    def __get__(descriptor, instance, owner):
        return descriptor.__dict__[instance]
    def __set__(descriptor, instance, value):
        descriptor.__dict__[instance] = value
    def __set_name__(descriptor, instance, value):
        pass


def ex15():
    """ Factory that wraps functionality

    * specify behavior on the descriptor
    * have factory return descriptor
    * give factory descriptor to class
    """

    class Person(object):
        def __init__(self, name):
            self.name = name

        @MartialArt('swords')
        @MartialArt('claws')
        @MartialArt('staff')
        def martial_art(self):
            pass
    assert Person('Tyler').martial_art.swords

ex15();
 
class MartialArt(object):
    def __get__(descriptor, instance, owner):
        return descriptor.__dict__[instance]
    def __set__(descript
