import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Unicode, Bool, Any, List, Instance, \
           Property, cached_property, on_trait_change

from traitsui.api \
    import View, Item, Group, VGroup, HGroup, Label, spring, \
           Handler, Action, Menu, MenuBar, ToolBar, StatusItem, \
           ListEditor, TreeEditor, TreeNode, ObjectTreeNode

from traitsui.menu \
    import OKButton, CancelButton

from pyface.api \
    import ImageResource, confirm, error, warning, YES, NO, CANCEL, OK, \
           FileDialog, DirectoryDialog, confirm, error, warning, YES, NO, \
           CANCEL, OK, ImageResource, FilePosition, FileInfo, ImageResource, \
           GUI, AboutDialog, ProgressDialog, SplashScreen, SplitApplicationWindow, \
           PythonShell, Toolkit, OKCancelButtons, OKButton, CancelButton, \
