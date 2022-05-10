import gc, weakref
from pymol import cmd, CmdException

def __init__(self):
    self.menuBar.addmenuitem('Plugin', 'command',
                             'Show all objects',
                             label = 'Show all objects',
                             command = lambda s=self : showallobjects(s))

def showallobjects(app):
    """
    DESCRIPTION

    Show all objects in the scene.
    """
    cmd.delete('*')
    cmd.refresh()

cmd.extend('showallobjects', showallobjects)
