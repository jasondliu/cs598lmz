import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class TIMECAPS(ctypes.Structure):
    _fields_ = [("wPeriodMin", ctypes.wintypes.UINT),
                ("wPeriodMax", ctypes.wintypes.UINT)]

timeGetDevCaps = ctypes.windll.winmm.timeGetDevCaps
timeGetDevCaps.argtypes = [ctypes.POINTER(TIMECAPS), ctypes.c_uint]
timeGetDevCaps.restype = ctypes.c_uint

# Get the constants.
wTimerRes = ctypes.c_uint(0)

timeGetDevCaps(ctypes.byref(wTimerRes), ctypes.sizeof(wTimerRes))
wTimerRes = wTimerRes.value

# Set the timer resolution to the minimum for the system.
timeBeginPeriod = ctypes.windll.winmm.timeBeginPeriod
timeBeginPeriod(wTimerRes)

timeEndPeriod = ctypes.windll.winmm.timeEndPeriod

# Set the timer
timeSetEvent
