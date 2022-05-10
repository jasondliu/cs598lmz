import io
class File(io.RawIOBase):
    """
    A file-like object that writes to a list of strings.
    """
    def __init__(self):
        self.content = []

    def write(self, s):
        self.content.append(s)

    def getvalue(self):
        return b''.join(self.content)

def get_ipython():
    """
    Get the IPython instance.
    """
    try:
        return get_ipython()
    except NameError:
        return None

def set_ipython(ip):
    """
    Set the IPython instance.
    """
    global _ipython
    _ipython = ip

def get_ipython_display():
    """
    Get the IPython display.
    """
    ip = get_ipython()
    if ip is None:
        return None
    return ip.display_formatter.format

def set_ipython_display(display):
    """
    Set the IPython display.
    """
    global _ipython_display
    _ipython_display = display


