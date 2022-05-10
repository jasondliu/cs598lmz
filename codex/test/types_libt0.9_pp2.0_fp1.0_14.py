import types
types.ListType = types.UnicodeType

VIDEO_PREFIX = "/video/pbsvideo"

####################################################################################################

def Start():

	Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, "PBS", "icon-default.png", "art-default.png")

	Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
	Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

	Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")

	ObjectContainer.title1 = "PBS"
	ObjectContainer.view_group = "List"

	HTTP.CacheTime = CACHE_1HOUR
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.4) Gecko/20100611 Firefox/3.6.4'
	
####################################################################################################
