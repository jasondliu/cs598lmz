import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

# start the PyQt application
app = QApplication(sys.argv)
# create the main window object and show it
window = MainWindow()
window.show()

# start the event loop
sys.exit(app.exec_())
</code>

