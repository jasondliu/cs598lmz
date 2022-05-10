import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"myappid")

class Video:
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.play_status = False
        self.play_btn = tk.Button(self.root, text="Play", command=self.play_video)
        self.play_btn.place(height=30, width=60, x=10, y=50)
        self.stop_btn = tk.Button(self.root, text="Stop", command=self.stop_video)
        self.stop_btn.place(height=30, width=60, x=80, y=50)
        self.pause_btn = tk.Button(self.root, text="Pause", command=self.pause_video)
        self.pause_btn.place(height=30, width=60, x=150, y=50)
        self.resume_btn = tk.Button(self.root, text="Resume", command=self.resume
