import socket
import urllib2
import xml.dom.minidom as minidom
import xml.sax as sax

class CinequestMovieHandler(sax.ContentHandler) :
  def __init__(self, result) :
    self._event = ""
    self._result = result
    self._in_permalink = False
    self._in_largeImage = False
    self._in_image = False
    self._in_cast = False
    self._in_director = False
    self._in_film = False
    self._in_festival = False
    self._in_reviewer = False

  def _add_element(self, element) :
    if self._in_permalink :
      self._result['permalink'] = element
    if self._in_largeImage :
      self._result['largeImage'] = element
    if self._in_image :
      self._result['image'] = element
    if self._in_cast :
      self._result['cast'].append(element)
    if self._in_director :
      self._result
