from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'I 2s f')
s.__setattr__('size', s.size)
s.__setattr__('pack', lambda *x: s.pack(*x))
s.__setattr__('unpack', lambda *x: s.unpack(*x))
s.__setattr__('pack_into', lambda *x: s.pack_into(*x))
s.__setattr__('unpack_from', lambda *x: s.unpack_from(*x))
#}

class Mouse(object):
    '''
    This class represents a mouse
    '''
    def __init__(self, user = None, input = None, passphrase = None,
                 bufsize = 4096, wheels = [0, 0]):
        if user is None:
            self.user = self.get_user()
        else:
            self.user = user

        if input is None:
            self.input = self.get_input()
        else:
            self.input = input

        if passphrase is None:
            self
