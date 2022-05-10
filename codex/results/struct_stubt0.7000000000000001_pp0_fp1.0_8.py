from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bcc')
s.pack(b'\x00', b'\x01', b'\x02')

# from _strptime import _strptime_datetime
# _strptime_datetime.__init__([], dict(year=1997, month=9, day=15))

# from _thread import allocate_lock
# allocate_lock.__init__()

# from _thread import get_ident
# get_ident.__init__()

# from _thread import stack_size
# stack_size.__init__([], dict(size=0))

# from _thread import start_new_thread
# start_new_thread.__init__([], dict(function=None, args=[], kwargs=None))

# from _thread import interrupt_main
# interrupt_main.__init__()

# from _thread import exit
# exit.__init__([], dict(args=[], kwargs=None))

# from _thread import LockType
# LockType.__init__([], dict(locked
