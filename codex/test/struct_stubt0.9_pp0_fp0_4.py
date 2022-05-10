from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__("_fmt", "<5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s")
self.adj_struct.__init__("","","","","","","","","","","","","","","","",""),
self.adj_struct.__setattr__("_fmt", "<5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s5s")

# need to add values using self.adj_struct.__setitems__()

self.adj_struct.__setitem__(0, ("1  ","2  ","3  ","4  ","5  ","6  ","7  ","8  ","9  ","10 ","11 ","12 ","13 ","14 ","15 ","16 ","17 ","18 "))
