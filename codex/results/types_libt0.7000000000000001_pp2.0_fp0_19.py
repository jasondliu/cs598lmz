import types
types.FunctionType = (lambda: None).__class__

# A list of all the global variables used by the plugin
# This list only needs to be updated when new global variables are introduced
global_variables = ["cfg", "config", "db", "f", "g", "m", "meta", "plugin_info", "proxies", "reloaded", "request", "sleep", "th", "thread", "variables", "xbmc", "xbmcaddon", "xbmcgui", "xbmcplugin", "xbmcversion", "xbmcvfs"]

# A list of all the global variables that should be copied to all threads
# This list only needs to be updated when new global variables are introduced
shared_variables = ["cfg", "config", "db", "f", "meta", "proxies", "request", "variables", "xbmc", "xbmcaddon", "xbmcgui", "xbmcplugin", "xbmcversion", "xbmcvfs"]

def _import_global(module, name):
	"""
	Import a global variable from a
