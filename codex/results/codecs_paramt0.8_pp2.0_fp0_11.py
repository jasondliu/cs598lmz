import codecs
codecs.register_error('replace_python3', lambda e: (u'\ufffd', e.start + 1))

class TvrageShows:
    """
    Reads the tvrage available shows from a file, this is to prevent
    tvrage from being hammered with api calls all the time. If no file is
    specified it will try to use the automatically created shows.txt.
    
    :param filename: Filename of the shows file
    :type filename: string
    """
    def __init__(self, filename=None):
        # default filename
        if filename == None:
            filename = os.path.join(addon.data_path, 'shows.txt')

        # read tvrage shows
        f = codecs.open(filename, 'r', 'utf-8', 'replace_python3')
        self.shows = json.load(f)
        f.close()
    
    def getTvrageIdForShow(self, show):
        """
        Searches the shows tvrage id. It uses a simple (and not 100% accurate)
        search based on comparing the show name.

