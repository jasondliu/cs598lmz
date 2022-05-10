import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
 
def get_app():
    app = QApplication(sys.argv)
    return app

def get_window():
    window = QMainWindow()
    return window

def set_window_title(window, title):
    window.setWindowTitle(title)

def set_window_size(window, width, height):
    window.resize(width, height)

def set_window_icon(window, icon_path):
    window.setWindowIcon(QIcon(icon_path))

def set_window_position(window, x, y):
    window.move(x, y)

def set_window_background_color(window, r, g, b):
    color = QColor(r, g, b)
    window.setAutoFillBackground(True)
    palette = window.palette()
    palette.setColor(window.backgroundRole(), color)
    window.setPalette(palette)

def set_window_tooltip
