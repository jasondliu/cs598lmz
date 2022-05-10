import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def getHandle(checkIn,userAgent):
    handler = request.HTTPHandler(debuglevel=0);
    opener = request.build_opener(handler);
    if checkIn is True:
        loginIn = '?login='+userAgent
    else:
        loginIn = ''
    opener.addheaders = [('User-Agent',userAgent+loginIn)];
    request.install_opener(opener);

def getData(fangUrl,pageUrl):
    fangUrl = fangUrl+pageUrl;
    print 'getData from '+fangUrl;
    data = request.urlopen(fangUrl);
    dataContent = str(data.read());
    print 'success getData from '+fangUrl;
    return dataContent;

def getPageInfo(htmlContent):
    pattern_pageInfo = re.compile('<div class="list.*?page_info">.*?<b>(.*?)</b>.*
