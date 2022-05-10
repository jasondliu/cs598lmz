import weakref
# Test weakref.ref(Circle())
# without __del__ method
# if Circle() can reference to itself correctly
class Circle(object):
    def __init__(self):
        print 'A circle is born.'
        self.area =  3.14 * 4
    def __del__(self):
        print 'I will die.'
#         pass


if __name__ == '__main__':
    c = Circle()
    print repr(c)
    # => '<__main__.Circle object at 0x10243c810>'
    print c.area
    # => 12.56

    # It need to write __del__ function to delete object
    print 'Delete object:'
    del c # c = None
    # print 're-print object c:',c
    # NameError: name 'c' is not defined
