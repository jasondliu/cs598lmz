import types
types.ClassType

#Extentions and notations

l = [1,2,3]
l.append(4)
l

l.count(3)

#It's important to understand what's happening so that you can use this mechanism in your own code

# Creating extensions types.

class MyList(list):
    pass


class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))


l = MyList([1,2,3,4])
l

l.remove_min()
l

l = MyList([1,2,3,4])
l.remove_max()
l


class MyList(list):
    def remove_min(self):
        self.remove(min(self))

