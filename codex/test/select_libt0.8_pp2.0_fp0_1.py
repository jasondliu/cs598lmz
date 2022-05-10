import select_season

class Select_Date_Season(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Select_Date_Season, self).__init__(parent)
        self.ui = Ui_select_date_season()
        self.ui.setupUi(self)

        self.ui.DateEdit_season_start.setDate(QtCore.QDate.currentDate())
        self.ui.DateEdit_season_end.setDate(QtCore.QDate.currentDate())
        self.ui.DateEdit_season_start.dateChanged.connect(self.on_date_changed)

    #期间更改时，结束日期禁止小于开始日期
