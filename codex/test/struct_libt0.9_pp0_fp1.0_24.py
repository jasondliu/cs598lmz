import _struct as struct

# noinspection PyUnusedLocal
def sliderHint(value):
    return '%d' % math.pow(10, 0.5 * value)


def nuboolToText(value):
    if value:
        return u'Да'
    else:
        return u'Нет'


def onSelectHospital(widget, data='*'):
    global clientId
    hospitalId = data
    if hospitalId == '*' and len(hospitalIdList) > 1:
        return
    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
