import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H'),daemon=True).start()

class BaseWidget(object):
    def __init__(self, parent, height, width, y, x, **kwargs):
        self.height, self.width = height, width
        self.win = curses.newwin(height, width, y, x)
        self.parent = parent
        self.parent.add(self)
        self.par = None

class SrcList(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.win.border()
        self.win.addstr(0, 10, "SOURCE LIST")
        self.win.refresh()
        self.nodelist = NodeList(self, self.height-2, self.width-2, 1, 1)
    def add(self, widget):
        if isinstance(widget, NodeList):
            self.nodelist = widget
        self.nodelist
