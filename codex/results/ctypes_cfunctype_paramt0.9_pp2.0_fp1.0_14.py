import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool,ctypes.c_uint,ctypes.c_uint,
                                   ctypes.c_uint,ctypes.c_uint)

def set_callback_interval(interval):
    RfRet = rfid.SetCommuImmeTimeout(rfreader, 0)
    time.sleep(0.1)
    start_time = time.time()
    RfRet = rfid.SetCommuImmeTimeout(rfreader, 1)
    timelapse = time.time() - start_time
    print("time lapse: " + str(timelapse))
    return


def read_data():
    read_packet = ctypes.c_void_p(rfid.EpcGen2_CreateReadPacket())
    read_packet_len = ctypes.c_uint32(0)
    read_packet_len_real = ctypes.c_uint32(0)
    read_packet_list = ctypes.c_void_p(rfid.Rfid_CreatePacketList())

   
