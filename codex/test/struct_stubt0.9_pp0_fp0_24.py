from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', byteorder='little', _per_sync=166)
# s.__init__('Bhhl', byteorder='little', _per_sync=166)

def motor_pack(h):
    return s.pack(*h)

def motor_unpack(d):
    return s.unpack(d)

def motor_unpack_all(d):
    return [s.unpack(i) for i in chunk_data(d, sync=166)]

def pack_current_task(cmd):
    if issubclass(cmd.__class__, BaseTask):
        s = cmd.__class__
        if issubclass(cmd.__class__, Task):
            kk = cmd.__dict__
            # kk.pop('motor_left_speed')
            # kk.pop('motor_right_speed')
            kk.pop('speed')
            kk.pop('servo_pan')
            kk.pop('servo_tilt')
            vv = kk.values()
