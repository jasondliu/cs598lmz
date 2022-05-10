import codecs
codecs.register(getregentry())

from cStringIO import StringIO

from xml.dom.minidom import parseString

from htmlentitydefs import entitydefs

def _fix_up_html(text):
    # replace &apos; entities with apostrophes
    text = text.replace(u'&apos;', "'")
    # replace &quot; entities with apostrophes
    text = text.replace(u'&quot;', '"')
    # replace &gt; entities with '>'
    text = text.replace(u'&gt;', '>')
    # replace &lt; entities with '<'
    text = text.replace(u'&lt;', '<')
    # replace &amp; entities with '&'
    text = text.replace(u'&amp;', '&')
    # replace unknown entities with blanks
    text = re.sub('&[^;]+;', '', text)
    return text

def _fix_up_text(text):
    text = _fix_up_html(
