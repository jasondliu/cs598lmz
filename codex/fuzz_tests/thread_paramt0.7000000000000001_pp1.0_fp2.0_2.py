import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()


from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
from functools import partial
from itertools import izip
from itertools import islice
from itertools import tee
from multiprocessing import Pool
from multiprocessing import cpu_count
from os import path
from random import randint
from random import seed

from PyQt4.QtCore import QObject
from PyQt4.QtCore import QPointF
from PyQt4.QtCore import QRectF
from PyQt4.QtCore import QSizeF
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import SLOT
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QGraphicsView
from PyQt4.QtGui import QPolygonF
