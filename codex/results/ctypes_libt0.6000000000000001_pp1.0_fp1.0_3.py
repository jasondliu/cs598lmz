import ctypes
ctypes.windll.user32.MessageBoxW(0, "bla", "blub", 0)
</code>
This works fine.
When I try to do the same thing with a <code>QMessageBox</code>, I get the same error:
<code>import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
QtGui.QMessageBox.information(None, "bla", "blub")
</code>
I also tried to use <code>messageBox</code> instead of <code>information</code>, but with the same result.
I'm using PySide 1.2.2 on Windows 7 (64bit).
I'm also using a custom manifest file (to avoid the manifest merging issue).


A:

It seems that the problem goes away when I remove the manifest file.
So I guess it's a problem with the manifest.

