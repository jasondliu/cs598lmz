import types
types.MethodType(lambda self: self.setValue(self.value() + 1), QtGui.QSpinBox)
types.MethodType(lambda self: self.setValue(self.value() - 1), QtGui.QSpinBox)

types.MethodType(lambda self: self.setValue(self.value() + self.singleStep()), QtGui.QDoubleSpinBox)
types.MethodType(lambda self: self.setValue(self.value() - self.singleStep()), QtGui.QDoubleSpinBox)


def _spinbox_wheel_event(self, event):
    if event.delta() > 0:
        self.stepUp()
    else:
        self.stepDown()

QtGui.QSpinBox.wheelEvent = _spinbox_wheel_event
QtGui.QDoubleSpinBox.wheelEvent = _spinbox_wheel_event

# -----------------------------------------------------------------------------
# QSpinBox
# -----------------------------------------------------------------------------

class QSpinBox(QtGui.QSpinBox):
    def __init__
