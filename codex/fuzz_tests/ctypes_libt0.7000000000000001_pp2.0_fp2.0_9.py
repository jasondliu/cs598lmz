import ctypes
ctypes.windll.user32.SetProcessDPIAware()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def seperate_list(list):
    return map(int, list.replace(",", "").replace("|", "").replace("[", "").replace("]", "").split())


def list_to_string(list):
    return ', '.join(list)


def format_line(line):
    return line.replace("\n", "").replace("\r\n", "").replace("\r", "").split("\t")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Grafisch')
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet("background-color: #FFFFFF;")
        self.home()

    def home(self):

       
