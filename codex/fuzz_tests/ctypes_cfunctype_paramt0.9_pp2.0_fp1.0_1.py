import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# ################################################################################################################################

    # Dictionary for all signal handlers

# ################################################################################################################################

signal_dict = {
    'SIGABRT'    : None, # Function(sig) called on process abort signal
    'SIGALRM'    : None, # Function(sig) called when alarm goes off
    'SIGBUS'     : None, # Function(sig) called when system detects a bus error
    'SIGCHLD'    : None, # Function(sig) called when child process exits
    'SIGCONT'    : None, # Function(sig) called when process is continued
    'SIGFPE'     : None, # Function(sig) called when system detects a floating-point math error
    'SIGHUP'     : None, # Function(sig) called on system hangup
    'SIGILL'     : None, # Function(sig) called when system detects an illegal instruction
    'SIGINT'     : None, # Function(
