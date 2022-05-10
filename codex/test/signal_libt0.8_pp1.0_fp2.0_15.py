import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import pickle
import json
import threading

class StreamDisplayer:
    def __init__(self, label):
        self.widget = QTextEdit()
        self.widget.setReadOnly(True)
        self.widget.setMaximumHeight(150)
        self.label = label

    def write(self, text):
        self.widget.append(text)
    def flush(self):
        pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.bbox_xmin = QLineEdit()
        self.bbox_xmax = QLineEdit()
        self.bbox_ymin = QLineEdit()
        self.bbox_ymax = QLineEdit()
        self.save_bbox = QPushButton('Save bounding box')

        self.mask_idx = 0
