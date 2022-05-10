import _struct
import _string
import _curses
import _curses_panel

_curses_panel._initscr()
_curses.initscr()

_curses.typeahead(sys.stdin.fileno())
_curses.cbreak()
_curses.noecho()

_curses.start_color()

_curses.init_pair(1, _curses.COLOR_RED, _curses.COLOR_BLACK)
_curses.init_pair(2, _curses.COLOR_GREEN, _curses.COLOR_BLACK)
_curses.init_pair(3, _curses.COLOR_YELLOW, _curses.COLOR_BLACK)
_curses.init_pair(4, _curses.COLOR_BLUE, _curses.COLOR_BLACK)
_curses.init_pair(5, _curses.COLOR_MAGENTA, _curses.COLOR_BLACK)
_curses.init_pair(6, _curses.COLOR_CYAN, _curses.COLOR_BL
