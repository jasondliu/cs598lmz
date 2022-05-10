import threading
# Test threading daemon to initialise game-objects and game loop

# Initialize rootUI
class rootUI(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("sBBs")
        #self.root.geometry("800x600")
        self.menubar = tk.Menu(self.root)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.root.destroy)
        #editmenu = tk.Menu(self.menubar, tearoff=0)
        helpmenu = tk.Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label='About', command=self.about)
        self.menubar.add_cascade(label="File", menu=filemenu)
        #self.menubar.add_cascade(label="Edit", menu=editmenu)
        self.menubar.add_cascade(label="Help", menu=help
