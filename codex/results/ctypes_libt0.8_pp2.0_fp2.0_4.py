import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
</code>


A:

I think you are doing a lot of things wrong:

Your script is not a GUI but a console application. You don't use the GUI, so don't make it a GUI.
Running a script as admin is an OS thing, so don't include OS specific code in it by importing win32com.client.

An example of a real GUI, as a function, from my book:
<code>def get_settings():
    """Get the settings file."""
    filename, selector = QFileDialog.getOpenFileName(
        None, "Open Settings File",
        '', 'Settings (*.json)',
        options=QFileDialog.DontUseNativeDialog
    )
    if filename:
        with open(filename) as f:
            settings = json.load(f)
        return settings
</code>
