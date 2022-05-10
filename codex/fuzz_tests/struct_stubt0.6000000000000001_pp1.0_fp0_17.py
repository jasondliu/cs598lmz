from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<h'
s.size = 2

class Data(object):
    def __init__(self):
        self.data = []

    def add(self, x, y, z):
        self.data.append([x, y, z])

    def pack(self):
        s.format = '<h' + 'i'*len(self.data)
        s.size = 2 + 4*len(self.data)
        l = len(self.data)
        a = s.pack(l, *[j for i in self.data for j in i])
        self.data = []
        return a

    def __len__(self):
        return len(self.data)

data = Data()

def add_data(x, y, z):
    data.add(x, y, z)
    if len(data) == 65535:
        send_data()

def send_data():
    if len(data) == 0:
        return
    s.send(data.pack())

def close():
