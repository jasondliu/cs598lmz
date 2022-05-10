import lzma
lzma.LZMAError = IOError

from emtools.ccpu.opcodes import Opcodes
from emtools.ccpu.screen import Screen

##########
# screen #
##########

def test_screen_init(screen):
    pass

def test_screen_set_get(screen):
    screen.set(0, 0, 1)
    assert screen.get(0, 0) == 1
    screen.set(9, 9, 1)
    assert screen.get(9, 9) == 1

def test_screen_clear(screen):
    screen.set(0, 0, 1)
    screen.clear()
    assert screen.get(0, 0) == 0

def test_screen_render(screen):
    screen.set(0, 0, 1)
    assert screen.render() == """+-----------------+
|1                 |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
+-----------------+"""

def test_screen_render_error
