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
    try:
        if hospitalId == '*':
            table = db.table('Event')
        else:
            table = db.table('Event').join(db.table('OrgStructure'), db.table('OrgStructure_HospitalBed'),
                                           db.table('EventType'), 'LEFT', table['eventType_id'].eq('EventType.eventTypeId'))

