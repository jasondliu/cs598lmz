import signal
# Test signal.setitimer
setitimer.signal_handler(signal.SIGPROF)

# GUI-Independent Functions

def get_key(*args, **kw):
    """
    A hack to help using ctypes.
    """
    c = getch()
    if c:
        try:
            # if it's a command string, take the first character.
            c = c[0]
        except:
            pass
    return c

def signal_handler(sig_num, stack_frame):
    """
    Default signal handler (merely exits)
    """
    sys.exit()

def user_quit():
    """
    Handle user quitting.
    """
    # Note, during testing, I see that pressing CTRL-D causes
    # a "KeyboardInterrupt", so this function simply catches that
    # exception, so the program can be killed.
    try:
        c = get_key()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        if c == QUIT_CHAR:
            sys.exit(0)

def
