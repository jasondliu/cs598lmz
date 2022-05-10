import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
lib.zbar_processor_set_data_handler.argtypes = lib.zbar_processor_set_data_handler.argtypes[:2] + [FUNTYPE]

video_device_path = open('/dev/video0', 'rb').name

from cStringIO import StringIO
code_present = False
code_data = None
frame_data = None

def bcr(img):
    import pybarcode as pbc
    c = pbc.bcr(StringIO(img))
    info = c.scan()[0]
    return info.info

def pnge(i, fn='/tmp/zbar.png'):
    from PIL import Image, ImageEnhance
    rgb_im = Image.fromarray(i)
    sat = ImageEnhance.Color(rgb_im)
    sat.enhance(1.2).save(fn)

def pgc(fn):
    import subprocess
    subprocess.check_call(
