import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class context(object):
    def __init__(self):
        self.r = None

root = Tk(className='Splash Screen')
root.resizable(False, False)
root.overrideredirect(True)
root.bind("<Button-1>", lambda x: root.destroy())
root.bind("<Key>", lambda x: root.destroy())
root.bind("<Double-Button-1>", lambda x: root.destroy())

root.after(500, lambda : root.destroy())

root.canvas = Canvas(root, width=300, height=200, highlightthickness=0)
root.canvas.pack() 

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def onCanvasConfigure(event):
    canvas.itemconfigure("background", width=event.width, height=event
