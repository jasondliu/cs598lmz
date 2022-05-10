import threading
threading.stack_size(2**27)

import sys
sys.path.insert(0,'..')
import main_python

class Test_main(unittest.TestCase):
    def test_main(self):
        main_python.main()

if __name__ == '__main__':
    unittest.main()
