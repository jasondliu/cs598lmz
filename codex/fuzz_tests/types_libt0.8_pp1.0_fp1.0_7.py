import types
types.FunctionType

import types
types.MethodType

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
hasattr(obj, 'x') 

getattr(obj, 'x')
#obj.x

setattr(obj, 'y', 19)

hasattr(obj, 'y') 
#obj.y

fn = getattr(obj, 'power')
fn
fn()

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

from io import StringIO
fp = StringIO()

fp.write('Hello')
fp.write(' ')
fp.write('world!')
print (fp.getvalue())

from io import BytesIO
fp2 = BytesIO()

fp2.write('中文'.encode('utf-8'))
print (fp2.getvalue())

class Student(object
