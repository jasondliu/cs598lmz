import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# Value of x: [[ 0.  0.]
#  [ 0.  0.]]
# Type of x: <class 'numpy.ndarray'>


# #my example variables
num = np.arange(10)
num = np.array(num)
print(num)

# (1) <class 'numpy.ndarray'>
#(2) <class 'numpy.ndarray'>
#(3) <class 'numpy.ndarray'>
#(4) <class 'numpy.ndarray'>
#(5) <class 'numpy.ndarray'>
#(6) <class 'numpy.ndarray'>


# def test(x,c):
#     list_type = list()
#     for y in x:
#         list_type.append(type(y))
#     print('Value of x:', x)
#     print('Type of x:', type(y))

# a = [1,2,3,4]
# test(a,1)

