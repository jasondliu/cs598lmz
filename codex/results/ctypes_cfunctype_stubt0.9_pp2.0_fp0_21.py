import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object()
func=fun

class CreateResize_Dialog(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(CreateResize_Dialog, self).__init__(parent)
        self.resize=Ui_Dialog_Resize_Window.Resize_Window()
        self.resize.setupUi(self)
        self.resize.btn_Resize.clicked.connect(self.create_resize_window)
        self.resize.btn_Confirm.clicked.connect(self.save)
    def create_resize_window(self):
        self.resize.btn_Confirm.setEnabled(True)
        if self.resize.rd_Inches.isChecked():
            self.__setupInches()
        elif self.resize.rd_Cm.isChecked():
            self.__setupCm()
        elif self.resize.rd_Custom.isChecked():
            self.__setupCustom()
    

