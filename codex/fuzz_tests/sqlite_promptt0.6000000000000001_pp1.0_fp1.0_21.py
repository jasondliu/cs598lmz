import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('database.db', check_same_thread=False)

class Application(tk.Frame):
    """
    The main window of the application
    """

    def __init__(self, master=None):
        """
        Initialization of the application
        """
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        Creation of the widgets of the application
        """
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.add_media = tk.Button(self, text="Add media",
                                   command=self.add_media)
        self.add_media.pack(side="top")

        self.add_media_text = tk.Entry(self)
        self.add_media_text.pack(side="top")

        self.add_media_label = tk.Label(self, text="Media name
