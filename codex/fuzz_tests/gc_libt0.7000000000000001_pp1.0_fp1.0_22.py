import gc, weakref

class Env(dict):
    '''
    環境クラス
    '''
    def __init__(self, parent=None):
        self.parent = parent

    def __getitem__(self, name):
        if name in self:
            return self.get(name)
        elif not self.parent:
            raise NameError(name)
        else:
            return self.parent[name]

class Cell(object):
    '''
    セルクラス
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(
