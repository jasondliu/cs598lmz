import socket
import urllib2

class Grabber:
    """
    Grabber provides an interface for fetching images from a URL.
    """
    @classmethod
    def fetch(cls, url):
        """
        Fetch an image from the given URL.
        """
        while True:
            try:
                return urllib2.urlopen(url).read()
            except urllib2.HTTPError:
                print("HTTPError({0}): {1}".format(e.errno, e.strerror))
            except urllib2.URLError:
                print("URLError({0}): {1}".format(e.errno, e.strerror))
            except socket.timeout:
                print("socket.timeout")


class Imager:
    """
    Imager provides an interface for generating images from a source image.
    """
    def __init__(self, source):
        self._source = source

    def to_image(self):
        """
        Convert a source to a PIL.Image.
       
