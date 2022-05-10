import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p);

#import tensorflow as tf
#import sys, os
#sys.path.append(os.path.abspath("./tftools"))
#import tftools

class TFModel:
    def __init__(self):
        self.sess = None
        self.saver = None
        self.saver_ckpt = None
        self.restore = 0

    def set_dir(self, sdir):
        # return a full path to dir/filename
        if sdir[len(sdir)-1] != '/':
            sdir += '/'
        return sdir

    def set_ckpt(self, ckpt):
        # return a full path to dir/ckpt-#
        if ckpt[0:5] != 'ckpt-':
            ckpt = 'ckpt-'+ckpt
        return ckpt
    
    def set_saver(self, sess, ckpt, ckpt_path):
        self.restore = 0
        c
