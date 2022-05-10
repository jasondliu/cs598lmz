import types
types.ClassType = type

class Wrapper(object):
    def __init__(self):
        self.children = []

    def AddChild(self, child):
        self.children.append(child)

    def GetNumChildren(self):
        return len(self.children)

    def HasChildren(self):
        return len(self.children) > 0

    def GetTypeName(self):
        return self.__class__.__name__

    def GetRoot(self):
        return self

    def FindItem(self, item):
        #logging.debug('FindItem: %s %s', item.GetTypeName(), item.GetValue())
        if self == item:
            return self
        for child in self.children:
            ret = child.FindItem(item)
            if ret:
                return ret
        return None

class OASISImage(Wrapper):
    def SetImage(self, image):
        self.image = image
    def GetImage(self):
        return self.image

