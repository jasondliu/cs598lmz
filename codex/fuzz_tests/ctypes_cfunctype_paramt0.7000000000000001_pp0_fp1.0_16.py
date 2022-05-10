import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def delete_callback(cnt):
    print('delete {}'.format(cnt))
CALLBACK = FUNTYPE(delete_callback)

def py_delete_callback(cnt):
    print('py_delete {}'.format(cnt))

def py_delete_callback2(cnt):
    print('py_delete {}'.format(cnt))

def py_delete_callback3(cnt):
    print('py_delete {}'.format(cnt))


class MyClass(object):
    def pydel(self, cnt):
        print('py_delete {}'.format(cnt))
    def pydel2(self, cnt):
        print('py_delete {}'.format(cnt))
    def pydel3(self, cnt):
        print('py_delete {}'.format(cnt))

class PyClass(object):
    def pydel(self, cnt):
        print('py_delete {}'.format(cnt))
    def pydel2(self, cnt):

