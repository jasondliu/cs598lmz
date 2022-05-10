import ctypes
ctypes.cdll.LoadLibrary("d:/bico/build/bin/VC/libbicocl/segment_test.dll")

import ctypes
libc = ctypes.WinDLL("msvcrt")
print('loaded')

import numpy as np

def run_bico_by_path_and_smooth_fac(df, path, smooth_fac):
    # init C segmenter
    hSegmenter = ctypes.c_void_p()

    # make sure data buffer is written in order of x0,x1,...,y0,y1,...
    data = np.array(df, dtype=np.float64)
    data_buffer = np.ascontiguousarray(data).ctypes.data
    num_data = len(df)
    bico_smooth_factor = smooth_fac

    print('Init segmenter')
    bicos.InitSegmenter(ctypes.c_void_p())


    print('Storing path on segmenter')
    bicos.AddPath(hSegmenter, path.ctypes
