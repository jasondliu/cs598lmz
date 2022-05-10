import codecs
codecs.register(xbmc.getSupportedMedia('video/x-matroska;codecs="' + codec + '"').decode("utf-8"))

def downloadSubtitles(id):
	post = {"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShowDetails", "params": {"tvshowid": int(id), "properties": ["file"]}, "id": 1}
	encoded_post_data = json.dumps(post).encode('utf-8')
	request = urllib.request.Request(url, data=encoded_post_data)
	request.add_header('Content-Type', 'application/json')
	response = urllib.request.urlopen(request)
	rsp = response.read().decode('utf-8')
	response.close()
	tvshow = json.loads(rsp)['result']
	path = tvshow['tvshowdetails']['file']
	movie = xbmc.translatePath(os.path.join(path, "video_ts.ifo"
