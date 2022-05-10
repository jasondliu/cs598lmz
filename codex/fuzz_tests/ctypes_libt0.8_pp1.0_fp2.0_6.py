import ctypes
ctypes.windll.qtwrapper.qtwrapper.loadUi('ui/qtwrapper.ui', w)

w.show()

sys.exit(app.exec_())
