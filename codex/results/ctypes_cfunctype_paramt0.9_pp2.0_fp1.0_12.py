import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.py_object)  # NOTE: py_object (or generic Python object) must be used here to permit std::function<void> to be wrapped by this functions


# NOTE: because of the way Cython works, the functions below must be implemented in Cython (instead of in pure Python code)
@FUNTYPE
def show_hide_callback_wrapper(unused_callback, frame, start, sim_time, unused_interval):  #real_nsec_frame_start, real_nsec_start, real_nsec_now, real_nsec_interval):
    if not start:
        frame.show()
        return
    # TODO: simulate the show_hide_effect_parameter.duration
    # now = real_nsec_now
    # frame_start = real_nsec_frame_start
    # elapsed = now - frame_start
    # eff_duration = show_hide_effect_parameter.duration
    # goal = frame_start + eff_duration
    # fraction = float(elapsed)/eff_duration
    # if __debug__:

