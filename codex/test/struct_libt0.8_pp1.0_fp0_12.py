import _struct
import fcntl
import sys

hide_stdin = None


def set_hide_stdin(hide):
    global hide_stdin
    hide_stdin = hide


def hide_stdin():
    hide_stdin
    return hide_stdin


def print_log(level, msg, *args):
    if hide_stdin is not None:
        return
    if args:
        msg = msg % args
    if level == "DEBUG":
        sys.stderr.write("DEBUG: %s\n" % msg)
    elif level == "INFO":
        sys.stderr.write("INFO: %s\n" % msg)
    else:
        sys.stderr.write(level + ": " + msg + "\n")

def set_stdin_to_nonblock():
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

