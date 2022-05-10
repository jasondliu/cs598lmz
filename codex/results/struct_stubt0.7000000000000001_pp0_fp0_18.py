from _struct import Struct
s = Struct.__new__(Struct)
s.format = "l"
s.size = 4
def unmarshall(s, file):
    return s.unpack(file.read(s.size))[0]

def marshall(s, value):
    return s.pack(value)

def unmarshall_data(file):
    return unmarshall(s, file)

def marshall_data(value):
    return marshall(s, value)


class SingleLinkedList:
    def __init__(self):
        self._data = None
        self._next = None

    def __str__(self):
        if self._data:
            return str(self._data)
        return 'None'

    def append(self, data):
        if self._data:
            if self._next:
                self._next.append(data)
            else:
                self._next = SingleLinkedList()
                self._next.append(data)
        else:
            self._data = data

    def size(self):
        size = 0
        if self._data:

