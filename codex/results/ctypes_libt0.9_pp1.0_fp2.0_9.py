import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'rk-discovery-tool')

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("error: "+str(e))
        pass
