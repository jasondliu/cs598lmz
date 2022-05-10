import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)



#크롤링 함수 구현하기
def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')

            return ret

    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 2]
def getWeatherURL(day_time):
    end_point = "http://newsky2.kma.go.kr/service/Sec
