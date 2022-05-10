import codecs
codecs.register_error('strict', codecs.ignore_errors)


if sys.platform == 'darwin':
    # OSX needs a workaround for the bug in the curses module
    def _initscr():
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i, i, -1)
        return stdscr
    curses.initscr = _initscr


class DummyInput(object):
    """
    Dummy input for controlling the application from test cases.
    """
    def __init__(self):
        self.input_queue = deque()
        self.screen = None
        self.key_dispatch = {}

    def add_keypress(self, key):
        self.input_queue.append(key)

    def register_key(self, key, handler):
        self.key_dispatch[key] = handler

    def run(self):
        while True:
            try:
               
