import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
sqlite3.connect(':memory:')
# Test ctypes.util.find_library()
ctypes.util.find_library('c')
# Test threading.Thread()
threading.Thread(target=lambda: None).start()

# Test os.getcwd()
os.getcwd()

# Test os.listdir()
os.listdir('.')

# Test os.stat()
os.stat('.')

# Test os.getenv()
os.getenv('PATH')

# Test os.urandom()
os.urandom(10)

# Test sys.argv
sys.argv
""")


class Python2LibraryTest(TestCase):
    def setUp(self):
        self.python_library_loader = PythonLibraryLoader()

    def test_load_library(self):
        self.assertIsInstance(self.python_library_loader.load_library('os'), Library)

    def test_load_library_with_different_name(self):
        self.assertIsInstance(self.python_library
