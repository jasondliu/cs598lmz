import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Start the main loop
app = QtGui.QApplication(sys.argv)

# Ensure we have a proper style sheet set
# from openalea.vpltk.qt import qt_style
# if qt_style.get_style() == 'custom':
#     qt_style.set_style('plastique')
# if qt_style.get_style() == 'cleanlooks':
#     import qdarkstyle
#     app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))

# from openalea.core.plugin.gui import PluginManagerWidget
# pm = PluginManagerWidget(session=session)
# pm.show()

from openalea.core.plugin.manager import PluginManager
pm = PluginManager()
# pm._refresh_metadata()
# pm.refresh_all()
# pm.install(package_filter='scons*')
# pm.remove(package_filter='scons*')
#
