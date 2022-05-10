import select
# Test select.select() here


# http://stackoverflow.com/questions/18124181/python-socket-buffer-bytes-to-string-with-backspace-characters
class TermProto(asynchat.async_chat):
    """
        This will hold the main functionality.
        """
    def __init__(self, sock, room=None):
        asynchat.async_chat.__init__(self, sock)

        try:
            (self.ibuf, self.obuf, self.ebuf) = sock
        except:
            self.ibuf = ""
            self.obuf = ""
            self.ebuf = ""

        self.nick = None
        self.set_terminator('\n')
        self.raw = False
        self.mode = 'ascii7'

        #self.data = []
        self.data = ""
        self.sigwinch = False


    def collect_incoming_data(self, data):
        """Buffer the incoming data while there's no terminator."""
        self.ibuf +=
