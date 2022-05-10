import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

import sys

app = QApplication(sys.argv)

player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("/home/pi/Videos/video.mp4")))

videoWidget = QVideoWidget()
player.setVideoOutput(videoWidget)

videoWidget.show()
player.play()

sys.exit(app.exec_())
