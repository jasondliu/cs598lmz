import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt5 Window")
        self.setGeometry(100, 100, 640, 480)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
</code>
If I run this code, I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\test.py", line 17, in &lt;module&gt;
    window = Window()
  File "C:\Users\Admin\Desktop\test.py", line 12, in __init__
    self.show()
TypeError: show() missing 1 required positional argument: 'self'
</code>
Why does this error occur and how can I fix it?


A:

You are using PyQt5 and the correct way
