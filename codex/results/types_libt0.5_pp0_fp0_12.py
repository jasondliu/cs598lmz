import types
types.ClassType = type

from . import _curses

import _curses_panel
import curses.wrapper

# The following variables are imported from _curses:
#
# addch, addstr, attroff, attron, attrset, baudrate, beep, bkgd, bkgdset,
# can_change_color, cbreak, clear, clearok, clrtobot, clrtoeol, color_content,
# color_pair, curs_set, def_prog_mode, def_shell_mode, delay_output, delch,
# deleteln, delscreen, derwin, doupdate, echo, echochar, endwin, erasechar,
# erasechar, filter, flash, flushinp, get_wch, get_wstr, getbkgd, getch,
# getmouse, getstr, getwin, halfdelay, has_colors, has_ic, has_il, has_key,
# hline, idcok, idlok, immedok, inch, initscr, inopts, intrflush,
