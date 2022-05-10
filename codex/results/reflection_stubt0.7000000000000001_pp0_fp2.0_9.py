fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = gi.gi_frame.f_code.co_freevars
fn()
 
#!/usr/bin/env python
# 
# bytearray_fromhex_oob.py
# 
# Copyright (c) 2014 by Cisco Systems, Inc.
# All rights reserved.

class Foo(object):
    def __init__(self, length):
        self.length = length

    def __getitem__(self, key):
        if key < self.length:
            return 1
        else:
            raise IndexError("")

    def __len__(self):
        return self.length

foo = Foo(4)
foo.length = -4
bytearray.fromhex("7f"*10 + "80"*10, foo)
 
#!/usr/bin/env python
# 
# bytearray_index_oob.py
# 
# Copyright (c) 2014 by Cisco Systems, Inc.
# All rights reserved.

class Foo(object):
    def
