import _struct

from . import dsz
from . import dsz.cmd
from . import dsz.data
from . import dsz.lp

class Process(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.ProcessItem = Process.ProcessItem(dsz.cmd.data.Get('ProcessItem', dsz.TYPE_OBJECT)[0])
        except:
            self.ProcessItem = None

        return

    class ProcessItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.commandline = dsz.cmd.data.ObjectGet(obj, 'commandline', dsz.TYPE_STRING)[0]
            except:
                self.commandline = None

            try:
                self.description = dsz.cmd.data.ObjectGet(obj, 'description', dsz.TYPE_STRING)[0]
