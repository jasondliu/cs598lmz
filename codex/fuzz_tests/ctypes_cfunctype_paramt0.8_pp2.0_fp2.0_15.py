import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

#

import multiprocessing
manager = multiprocessing.Manager()
queue = manager.Queue()

#

def Process(fn, arg=None):
	fn = FUNTYPE(fn)
	old = ctypes.windll.user32.SetWindowsHookExA(
		13, fn, ctypes.windll.kernel32.GetModuleHandleW(None), 0)
	print(old)
	if old != 0: ctypes.windll.user32.CallNextHookEx(old, 0, 0, 0)
	ctypes.windll.user32.UnhookWindowsHookEx(old)

#

def OnClick(nCode, wParam, lParam):
	print(queue.get())
	return ctypes.windll.user32.CallNextHookEx(0, nCode, wParam, lParam)

queue.put(1)

# Process(OnClick, 0)

#

def Notify(msg):
	ctypes.windll.user32.MessageBoxW(0, msg
