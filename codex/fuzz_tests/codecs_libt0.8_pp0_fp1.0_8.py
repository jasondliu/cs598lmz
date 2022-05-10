import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

HEADERS = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive',
}

SCHOOL_NAME_TO_URL = {
    "Xi'an Jiaotong University":
        'http://job.xjtu.edu.cn/portal/job/1/dgwzxx/dgwzxx.htm',
    "Northwestern Polytechnical University":
        'http://job.nwpu.edu.cn/col/col37970/index.html',
    "Xi'an University of Technology":
        'http://recruit.xaut.edu.cn:8080/recruit/',
    "Xidian University":
        'http://grs.xidian
