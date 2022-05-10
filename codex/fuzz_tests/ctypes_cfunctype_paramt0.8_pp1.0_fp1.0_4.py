import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

class get_star():

    def __init__(self):
        self.star = BinOcu(FUNTYPE(self.star_callback))
        self.star.Open()

    def star_callback(self,
                      target_id,
                      target_cx,
                      target_cy,
                      target_size,
                      target_pix,
                      target_sub_state):
        print("target_id:%d, target_cx:%d, target_cy:%d, target_size:%d, target_pix:%d, target_sub_state:%s" % (target_id,target_cx,target_cy,target_size,target_pix,target_sub_state))


if __name__ == '__main__':
    get_star()
    input()
