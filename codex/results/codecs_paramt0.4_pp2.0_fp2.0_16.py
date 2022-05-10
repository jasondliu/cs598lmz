import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_content(url):
    try:
        f = urllib2.urlopen(url)
        content = f.read()
        f.close()
        return content
    except urllib2.HTTPError, e:
        print 'HTTPError = ' + str(e.code)
        return None
    except urllib2.URLError, e:
        print 'URLError = ' + str(e.reason)
        return None
    except httplib.HTTPException, e:
        print 'HTTPException'
        return None
    except Exception:
        import traceback
        print 'generic exception: ' + traceback.format_exc()
        return None

def get_soup(url):
    content = get_content(url)
    if content:
        return BeautifulSoup(content)
    else:
        return None

def get_soup_from_file(filename):
    f = codecs.open(filename, encoding='utf-8', errors='strict')

