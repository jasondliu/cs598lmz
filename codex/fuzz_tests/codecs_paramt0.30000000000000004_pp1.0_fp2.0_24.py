import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
#   This is a simple example of a Python module that can be called by
#   Slicer's python interactor or another scripting language. The
#   interface is the same for all scripting languages. See the
#   documentation for the ScriptedLoadableModule class for more
#   information.
#
#   A ScriptedLoadableModule is a module that can be scripted in
#   Python. The scripted module contains a class that derives from
#   ScriptedLoadableModuleLogic with a method called hasImageData that
#   returns true if the module has an image to display.
#
#   A new ScriptedLoadableModule instance is created for each widget
#   that is opened. The hasImageData method is then called on the
#   instance to determine if there is a visible image available to
#   display. If hasImageData returns true then three widgets are
#   created:
#
#   1) A slicer.qMRMLTreeView that uses the DataProbe to show
#      information about the current voxel. This widget is placed in
#
