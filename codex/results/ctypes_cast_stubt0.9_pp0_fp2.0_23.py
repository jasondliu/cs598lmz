import ctypes
ctypes.cast(ctypes.pointer(var), ctypes.POINTER(ctypes.c_int64))
np.arange(10, dtype=np.float64)
np.arange(10, dtype=np.float32)


 
class NumPyCreator():
    #     instance_counter = 0
    #     def __init__(self):
    #         NumPyCreator.instance_counter += 1
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value=0):
        return value * np.ones(shape)

    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        return np.identity(n)


npc = NumPyCreator()

print(npc.from_
