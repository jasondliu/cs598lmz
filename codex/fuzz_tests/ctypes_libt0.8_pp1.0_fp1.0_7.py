import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabel_View = QtWidgets.QTableWidget(self.centralwidget)
        self.Tabel_View.setGeometry(QtCore.QRect(10, 40, 1160, 430))
        self.Tabel_View.setObjectName("Tabel_View")
        self.Tabel_View.setColumnCount(3)
        self.Tabel_View.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.Tabel_View.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
       
