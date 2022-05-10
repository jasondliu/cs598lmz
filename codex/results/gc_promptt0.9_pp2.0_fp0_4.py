import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect after an object in a container dies
#    tests gc.collect() on lists, dicts, and tuples


class Test_1():
    def __del__(self):
        gc.collect()

    def Test_1_1(self):
        lis = []
        for i in range(4):
            lis.append(weakref.ref(object()))
        self.Test_3(lis)

    def Test_1_2(self):
        dic = {}
        for i in range(4):
            dic[i] = weakref.ref(object())
        self.Test_3(dic.values())

    def Test_1_3(self):
        tup = []
        for i in range(4):
            tup.append(weakref.ref(object()))
            tup[i] = tup[i],
        self.Test_3(tup)

    def Test_1_4(self):
        st = {}
        for i in range(4):
            st[weakref.ref(object())]
