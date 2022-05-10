import ctypes
ctypes.windll.psapi.GetPerformanceInfo(ctypes.byref(perf_data), ctypes.sizeof(perf_data))
</code>
(The <code>ctypes</code> wrapper is not correct, but it should show the general idea.)

