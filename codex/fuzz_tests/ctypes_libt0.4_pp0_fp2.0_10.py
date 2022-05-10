import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Then set the window icon
import os
import sys
from PyQt5 import QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(os.path.join('images', 'icon.png')))
</code>
The problem is that the icon is not displayed in the taskbar. It is displayed in the window title bar and in the window icon in the taskbar, but not in the taskbar itself.

I have tried the following:

Adding a <code>QSystemTrayIcon</code> and setting the icon for it.
Setting the icon for the <code>QApplication</code> and <code>QMainWindow</code>.
Setting the icon for the application as described in the answer to this question.

None of these methods worked.
I am using Python 3.5, PyQt 5.7, and Windows 10.
What am I missing?


A:

I had the same problem
