import _struct
import time

# def saveFile(data, filename):
#     fp = open(filename, 'w')
#     fp.write(data)
#     fp.close()

# def readBinFile(filename):
#     fp = open(filename, 'rb')
#     data = fp.read()
#     fp.close()
#     return data

def readBinFile(filename):
    fp = open(filename, 'r')
    data = fp.read()
    fp.close()
    return data

def test_Array1():
    # test the array
    a = array.array('h',[1,2,3,4,5])
    print(a)
    print(type(a))

def test_Array2():
    # test the array
    a = array('h',range(0,10,2))
    b = array('h',range(1,11,2))
    c = array('h',range(0,10))
    print(a)
