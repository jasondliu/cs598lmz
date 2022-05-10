import codecs
codecs.register_error("strict", codecs.ignore_errors)


class SubsData:
    def __init__(self,
                 name="",
                 wordcount=0,
                 date="",
                 url="",
                 filename="",
                 extra="",
                 owner="",
                 lang="",
                 season="",
                 episode="",
                 comments="",
                 subtitleid="",
                 episodes=""):
        self.name = name
        self.wordcount = wordcount
        self.date = date
        self.url = url
        self.filename = filename
        self.extra = extra
        self.owner = owner
        self.lang = lang
        self.season = season
        self.episode = episode
        self.comments = comments
        self.subtitleid = subtitleid
        self.episodes = episodes


class OpenSubtitles:
    def __init__(self, useragent="OS Test User Agent"):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [("User-Agent", useragent)]
       
