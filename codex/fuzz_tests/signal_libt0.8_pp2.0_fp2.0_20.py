import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # This will allow C-c to terminate the program properly

class Test(BaseTest):
    app = QtGui.QApplication([])

    def test_str(self):
        self.assertEqual(str(QLineEdit()), "<QLineEdit ''>")
        self.assertEqual(str(QLineEdit('hello')), "<QLineEdit 'hello'>")

    def test_set_get_text(self):
        self.startQtApp()
        w = QLineEdit()
        w.setText('hello world')
        self.assertEqual(w.text(), 'hello world')
        w.setText('foo')
        self.assertEqual(w.text(), 'foo')
        self.stopQtApp()

    def test_clear(self):
        self.startQtApp()
        w = QLineEdit()
        w.setText('hello world')
        self.assertEqual(w.text(), 'hello world')
        w.clear()

