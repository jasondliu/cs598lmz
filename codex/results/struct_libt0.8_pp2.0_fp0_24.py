import _struct
import wave
import audioop
import pyaudio

from tkinter import *
import tkinter.ttk as ttk

from tkinter import filedialog

import wave
import pyaudio

class Gui:

    def __init__(self, root):
        self._root = root
        root.title("Sound Level Visualizer")

        self.recording = False
        self.paused = False
        self.playing = False
        self.stream = None
        self.wf = None
        self.p = None
        self.filepath = None

        self.frame = ttk.Frame(root)
        self.frame.pack()

        self.sound_bar = ttk.Progressbar(self.frame, orient=HORIZONTAL, length=500, mode='determinate')
        self.sound_bar.pack()
        self.sound_bar['maximum'] = 100
        self.sound_bar['value'] = 0

        self.recording_label = ttk.Label(self.frame, text="Not Recording")
        self.rec
