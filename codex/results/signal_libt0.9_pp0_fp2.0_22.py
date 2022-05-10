import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#qApp.exec_()
#sys.exit(qApp.exec_())
sys.exit(sys.exit(qApp.exec_()))
</code>
This is the error I get on terminal 
<code>QXcbIntegration: Cannot create platform OpenGL context, neither GLX or EGL are enabled
QOpenGLWidget: Failed to create context
QBitmap: Cannot create a QPixmap when no GUI is being used
QBitmap: Cannot create a QPixmap when no GUI is being used
QBitmap: Cannot create a QPixmap when no GUI is being used
QBitmap: Cannot create a QPixmap when no GUI is being used
</code>


A:

I mean it is possible to create simple gui with the gl widget
<code>from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from OpenGL import GL

import sys

class Window(QWidget):

    def __init
