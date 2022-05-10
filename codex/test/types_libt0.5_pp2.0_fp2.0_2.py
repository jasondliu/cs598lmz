import types
types.MethodType(lambda self: self.setValue(self.value() + 1), QtGui.QSpinBox)
types.MethodType(lambda self: self.setValue(self.value() - 1), QtGui.QSpinBox)

types.MethodType(lambda self: self.setValue(self.value() + self.singleStep()), QtGui.QDoubleSpinBox)
types.MethodType(lambda self: self.setValue(self.value() - self.singleStep()), QtGui.QDoubleSpinBox)

