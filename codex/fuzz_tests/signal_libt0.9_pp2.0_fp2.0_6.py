import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

main = QtWidgets.QApplication(sys.argv)
main.setOrganizationName(ORG_NAME)
main.setApplicationName(APP_NAME)
_ = lambda x: x

from ninja_ide import resources
from ninja_ide import core
from ninja_ide import gui
from ninja_ide.core.filesystem import filesystem_notifications
from ninja_ide.gui import main_panel


def launch_nogui():
    ''' Launch the IDE from another process (nogui) '''
    from ninja_ide.tools import call_commands
    from ninja_ide.core import settings
    from ninja_ide.core.logger import NinjaLogger

    settings.IS_NINJA_EXECUTING = True
    builtins.__dict__['IS_NINJA_EXECUTING'] = True

    ninjaide = core.ninja_ide()
    ui = ninjaide.load_ide()

    #GET THE FILE
    fileName = sys.arg
