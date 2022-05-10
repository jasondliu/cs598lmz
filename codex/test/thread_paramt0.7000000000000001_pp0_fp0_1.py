import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()
import inspect

def get_va_string(va):
    return (
        "['{}']".format(', '.join("{}={}".format(k, v)
            for k, v in sorted(va.items())))
        if va else ''
    )

def get_caller(frame_filter=None, frame=None):
    frame = frame or inspect.currentframe()
    tb = frame.f_back
    while tb:
        if frame_filter and frame_filter(tb):
            return tb
        tb = tb.f_back
    return frame

def log_frame(caller, va, level, color):
    if color is None:
        color = getattr(log_frame, 'color', None)
    if color:
        va = color(va)
