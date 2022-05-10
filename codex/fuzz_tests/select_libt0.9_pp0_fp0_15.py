import select
import tty

from boaconstructor.controllers.main_view_controller import MainViewController


class Terminal:
    """
    Terminal controls reading commands from shell and displaying text in target
    position.
    It is used in MainViewController.
    """
    def __init__(self):
        self.current_command = 0
        self.read = None
        self.stdin = sys.stdin
        self.old_tty = termios.tcgetattr(self.stdin)
        self.main_view_controller = MainViewController()

    def __enter__(self):
        self._set_tty_raw()
        return self

    def _set_tty_raw(self):
        tty.setcbreak(self.stdin.fileno())
        new = termios.tcgetattr(self.stdin)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
       
