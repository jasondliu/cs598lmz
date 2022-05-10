import weakref
from weakref import WeakSet
import xbmc
import xbmcaddon
import xbmcgui

try:
	from sqlite3 import dbapi2 as sqlite
	print("Loading sqlite3 as DB engine")
except:
	from pysqlite2 import dbapi2 as sqlite
	print("Loading pysqlite2 as DB engine")


__addon__ = xbmcaddon.Addon("service.skin.widgets")
__cwd__ = __addon__.getAddonInfo('path').decode("utf-8")
__profile__ = xbmc.translatePath( __addon__.getAddonInfo('profile') ).decode("utf-8")
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ) ).decode("utf-8")

__language__   = __addon__.getLocalizedString

sys.path.append (__resource__)

# class ServiceWindow(xbmcgui.WindowXMLDialog):
