import sys, threading

def run():
    thread = threading.Thread(target=runApp)
    thread.start()

def runApp():
    os.environ['TZ'] = 'UTC'
    time.tzset()

    QtGui.QApplication.instance().exec_()
    #sys.exit(app.exec())

os.environ['TZ'] = 'UTC'
time.tzset()

app = QtGui.QApplication(sys.argv)
screen = app.primaryScreen()
print("Width:",screen.width())
print("Height:",screen.height())

print("Available Colors:",QtGui.QColor.colorNames())

print("Available Aligns:",QtCore.Qt.AlignJustify)
print("Available Aligns:",QtCore.Qt.AlignAbsolute)
print("Available Aligns:",QtCore.Qt.AlignHorizontal_Mask)
print("Available Aligns:",QtCore.Qt.AlignVCenter)
print("Available Aligns:",QtCore.Q
