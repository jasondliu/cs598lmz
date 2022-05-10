import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int),
               ]
    def __str__(self):
        return "S(%d,%d,%d)" % (self.x, self.y, self.z)

class S2(ctypes.Structure):
    _fields_ = [("as1", ctypes.ARRAY(S, 10)),
              ]

class EventInfo(ctypes.Structure):
    _fields_ = [("myInt", ctypes.c_int),
                ("s", S),
                ("as2", ctypes.ARRAY(S, 10)),
               ]


# get rid of the ctypes Union!

def ff(eventInfo):
    eventInfo.myInt = 2
    eventInfo.s.x = 3
    eventInfo.as2[3].y = 5

ff(EventInfo(0, S(), (S() for i in range(10))))
