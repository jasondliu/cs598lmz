import gc, weakref
import pymel.core as pmc

## A callable class to handle the construction, updating, and deletion of the Preferences UI.
#
#  This class is instantiated as the last step in  the
#  pymel.tools.base.PymelBaseUI.setupUi method.
#
#  This class also handles wiring up the widgets' signals and slots to their corresponding
#  widget slot attributes.  Thus all signals from the <UI>_ui.py, and  the slots in the main plugin
#  file,  should be listed in the <UI>_ui.py file's setupUi method.  Below is an example of this
#  and the corresponding signal/slot.
#
#  @code
#  #  The signal connection in the setupUi method.
#  #  the 'btn' is the name of the widget, so the real signal name is 'btnClicked'
#  #  the '&PymelBaseUI' is the main plugin class, so the slot name is '&PymelBaseUI.doSomething'
#  self.connect( self.
