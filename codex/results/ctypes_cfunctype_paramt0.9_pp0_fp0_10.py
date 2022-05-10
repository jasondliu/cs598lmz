import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
_callback = None
def callback():
    _callback()
CBFUNC = FUNTYPE(callback)
def add_live_command(command, func):
    '''Add a live command, which updates values on the fly.'''
    global _callback
    _callback = func
    funcptr = CBFUNC()
    _commands[command] = func
    _lib.addLiveCommand(command.encode('utf-8'), funcptr)

def remove_live_command(command):
    '''Remove a live command. If a live command is removed while it is active,
    the command will stop.''
