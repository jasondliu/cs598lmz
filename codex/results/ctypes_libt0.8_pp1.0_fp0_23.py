import ctypes
ctypes.cdll.LoadLibrary('/usr/lib/libXp.so.6')
ctypes.cdll.LoadLibrary('/usr/lib/libXpm.so.4')
ctypes.cdll.LoadLibrary('/usr/lib/libXt.so.6')
ctypes.cdll.LoadLibrary('/usr/lib/libXmu.so.6')

# Needed by matplotlib in order to work properly.
os.environ['QT_API'] = 'pyqt'

# Needed to prevent matplotlib from crashing on exit.
os.environ['QT_DEBUG_PLUGINS'] = '1'

# silence warnings about matplotlib's GUI backend
import warnings
warnings.filterwarnings('ignore', '.*GUI is implemented.*', UserWarning)

# Needed by pygtk, see http://python-gtk-3-tutorial.readthedocs.org/en/latest/install.html
import locale
locale.setlocale(locale.LC_ALL, '')

import gtk
import matplot
