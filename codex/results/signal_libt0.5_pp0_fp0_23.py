import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Gestionnaire de mot de passe")
window.setWindowIcon(QIcon("images/logo.png"))
window.setMinimumSize(800, 600)
window.setMaximumSize(800, 600)
window.setStyleSheet("QMainWindow {background: url(images/fond.jpg) center center no-repeat;}")

widget = QWidget()
widget.setStyleSheet("QWidget {background: url(images/fond.jpg) center center no-repeat;}")
window.setCentralWidget(widget)

layout = QGridLayout()

label = QLabel("Gestionnaire de mot de passe")
label.setStyleSheet("QLabel {color: #ffffff; font-size: 30px; font-weight: bold; font-family: Arial;}")
layout.addWidget(label, 0, 0)

label2 = QLabel("Util
