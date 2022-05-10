import socket
import telnetlib
import select

# ============================================================== #
# ============================ GUI ============================= #
# ============================================================== #

class UserInterface(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.protocol('WM_DELETE_WINDOW', self.exit)

        self.bot = None

        self.frame = Frame(self)
        self.frame.grid()

        self.ip_label = Label(self.frame, text = "Client IP")
        self.ip_label.grid(column = 0, row = 1)

        self.ip_entry = Entry(self.frame)
        self.ip_entry.grid(column = 1, row = 1)

        self.port_label = Label(self.frame, text = "Port")
        self.port_label.grid(column = 0, row = 2)

        self.port_entry = Entry(self.frame)
        self.port_entry.grid(column = 1,
