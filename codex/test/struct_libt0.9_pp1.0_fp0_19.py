import _struct

class QLBar(object):
    def __init__(self, stian, bar_size, bar_type,
                 date, time, op, hi, lo, cl, vol, size, num, wap):

        self.__stian = stian
        self.__bar_size = bar_size
        self.__bar_type = bar_type
        self.__date = date
        self.__time = time
        self.__op = op
        self.__hi = hi
        self.__lo = lo
        self.__cl = cl
        self.__vol = vol
        self.__size = size
        self.__num = num
        self.__wap = wap

