import threading
threading.stack_size(102400)
import multiprocessing
multiprocessing.cpu_count()

import Tkinter as tk

from tempfile import gettempdir
import os.path
import random
import datetime
import pdb


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master.title("CNN-LSTM")

        self.vidPanelContainer = tk.Frame() # make a frame for the videos
        self.vidPanelContainer.grid(row=0, column=0, columnspan=4, rowspan=4, padx=10, pady=10)

        # creating one of each type of video player
        filename = get_latest_data_filename()
        # create the CNN-LSTM video
