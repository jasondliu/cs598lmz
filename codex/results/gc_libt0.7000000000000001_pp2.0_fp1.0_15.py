import gc, weakref
import si, si.test

if hasattr(gc, 'garbage'):
    def _get_garbage():
        return gc.garbage[:]
else:
    def _get_garbage():
        return []

def log_callback(text):
    si.test.logger.write('\n')
    si.test.logger.write(text)
    si.test.logger.flush()

class TestCase(si.test.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self._log_callback = log_callback
        self._log_callback('##############################\n')
        self._log_callback('### Starting %s\n' % self.getId())
    def tearDown(self):
        gc.collect()
        if _get_garbage():
            self._log_callback('### Garbage left: %s\n' % _get_garbage())
            self.fail('garbage left')
        self._log_callback('### Ending %s\n
