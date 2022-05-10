import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MouseHook(threading.Thread):
    def __init__(self):
        super().__init__()
        self.mouse_handle = None
        self.runnable = True

    def callback(self, nCode, wParam, lParam):
        if wParam == 0x201:
            self.mouse_handle.write('R'.encode())
        if wParam == 0x202:
            self.mouse_handle.write('L'.encode())
        return True

    def stop(self):
        self.runnable = False

    def run(self):
        self.mouse_handle = Mouse.Mouse()
        self.handler_func = FUNTYPE(self.callback)
        hook_handle = mouse_hook.SetWindowsHookExA(
            mouse_hook.WH_MOUSE_LL, self.handler_func, mouse_hook.GetModuleHandleA(None), 0)
        while self.runnable:
            mouse_hook.GetMessageA(None, 0, 0, 0)


class Mouse(object):
   
