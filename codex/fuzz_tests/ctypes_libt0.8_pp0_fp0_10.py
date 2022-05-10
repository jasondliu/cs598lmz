import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import os, sys
filename = os.path.join(os.path.dirname(__file__), "logo.ico")

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.text = "Python Email: Version 1.0\n"
        self.text += "Copyright (C) 2018 by almutlaq <sh.almutlaq@gmail.com>"
        self.text += "\n\nThis program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version."

        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(filename))
        self.setWindowTitle("About Python Email")
        self.setGeometry(300, 300, 350, 300)
        self.show()

if __name__ == '__main__':

