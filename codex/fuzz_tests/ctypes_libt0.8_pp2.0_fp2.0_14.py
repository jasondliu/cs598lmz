import ctypes
ctypes.pythonapi.PyOS_InputHook = ctypes.pythonapi.PyOS_InputHook
ctypes.pythonapi.PyOS_InputHook.argtypes = ()
ctypes.pythonapi.PyOS_InputHook.restype = ctypes.c_int

LONG_TIMEOUT = 60 * 60 * 2


class InheritableThread(threading.Thread):
    """
    A thread that inherits the parent thread's environment.
    """

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self.setDaemon(True)

    def run(self):
        env = os.environ.copy()
        env["HOST"] = "127.0.0.1"
        subprocess.call(["bash", "-c", "source /home/pi/Documents/scripts/env.sh; " + " ".join(self.args)],
                        shell=False, env
