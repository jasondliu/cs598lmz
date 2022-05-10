import ctypes
ctypes.cast(0, ctypes.py_object).value # durchwandert alle Referenzen auf einem Weg, aber geht nicht zurück

a = 2
a.__sizeof__()          # Größe auf 32-bit Plattform: 48 bytes
b = 1.3
b.__sizeof__()          # Größe auf 32-bit Plattform: 24 bytes
c = 'a'
c.__sizeof__()          # Größe auf 32-bit Plattform: 24 bytes
class Dummy(object): pass
d = Dummy()
d.__sizeof__()          # Größe auf 32-bit Plattform: 40 bytes
e = dict()
e.__sizeof__()          # Größe auf 32-bit Plattform: 240 bytes


id(dummy)     # Zeiger
type(dummy)   # Klasse an dessen Speicheradresse
isinstance(dummy, Dummy)    # True

class Person(object):
    def __init__(self
