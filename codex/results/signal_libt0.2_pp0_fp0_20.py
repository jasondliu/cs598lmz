import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QImage

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings

from settings import Settings
from video_player import VideoPlayer
from video_capture import VideoCapture
from video_writer import VideoWriter
from video_stream import VideoStream
from video_stream_thread import VideoStreamThread
from video_writer_thread import VideoWriterThread
from video_capture_thread import VideoCaptureThread
from video_player_thread import VideoPlayerThread

from image_processor import ImageProcessor
from image_processor_thread import ImageProcessorThread

from image_processor_factory import ImageProcessorFactory

from image_processor_settings import
