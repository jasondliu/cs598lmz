import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

import logging
logging.basicConfig(level=logging.DEBUG)

from components import gui


def main():
    app = gui.App()
    app.MainLoop()


if __name__ == '__main__':
    main()
</code>


A:

Turns out I just needed to add <code>wx.Frame</code> before <code>wx.App</code>. I don't why, but it works now.

