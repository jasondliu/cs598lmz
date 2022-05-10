import codecs
codecs.register_error("strict", codecs.ignore_errors)

def formatResponse(r):
    if r["type"] == "pdfurl":
        return "http://api.elsevier.com/content/article/%s?httpAccept=%s" % (r["doi"], r["content-type"])
    elif r["type"] == "fturl":
        return "http://api.elsevier.com/content/article/fulltext/%s?httpAccept=%s&apiKey=%s" % (r["doi"], r["content-type"], elsevier_api_key)
    else:
        return "[Error: unknown response type '%s']" % (r["type"])

def getEntries(doi):
    url = "http://api.elsevier.com/content/article/doi/%s?apiKey=%s" % (doi, elsevier_api_key)
    print url
    req = urllib2.Request(url)
    xml = urllib2.urlopen(req).read()
    dom = minidom.parseString(xml
