import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Sub-panels are panels defined in separate files in this directory.
# They must be loaded via this mechanism - they cannot be dynamically
# loaded at runtime.
#
import list
import series
import new
import edit
import delete
import saver

class Panel(gnomedvb.PanelBase):
    def __init__(self, app, notebook):
        gnomedvb.PanelBase.__init__(self, app, notebook, _("Series"))

        self.serieslist = list.Panel(app, notebook)
        self.seriesnew = new.Panel(app, notebook)
        self.seriesedit = edit.Panel(app, notebook)
        self.seriesdelete = delete.Panel(app, notebook)
        self.seriessaver = saver.Panel(app, notebook)

        self.serieslist.panel = self
        self.seriesnew.panel = self
        self.seriesedit.panel = self
        self.seriesdelete.panel = self
        self.seriessaver.panel
