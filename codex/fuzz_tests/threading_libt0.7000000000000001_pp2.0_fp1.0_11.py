import threading
threading.stack_size(2**27)

class SharedArray(object):
    def __init__(self, shape, dtype=np.float64):
        self.__dict__['shape'] = shape
        self.__dict__['dtype'] = dtype

        size = 1
        for d in shape:
            size *= d

        self.__dict__['mp_arr'] = multiprocessing.Array(dtype, size)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            index = np.ravel_multi_index(index, self.shape)
        return np.frombuffer(self.mp_arr.get_obj(), dtype=self.dtype)[index]

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            index = np.ravel_multi_index(index, self.shape)
        np.frombuffer(self.mp_arr.get_obj(), dtype=self.dtype)[index] = value

    def __array__(self):
       
