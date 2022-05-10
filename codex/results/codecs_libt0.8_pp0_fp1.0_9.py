import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

def __fetch_all_bus_data(http):
    url = 'http://bus.ke.qq.com/api/cms_list.php'
    return http.request('GET', url, fields={
        'v': '3',
        'cmd': 'getListByCategory',
        'cid': '7',
        'page': '0',
        'psize': '200'
    }).data

def fetch_all_bus_data(http):
    return json.loads(__fetch_all_bus_data(http))

def fetch_all_bus_company(http):
    return [bus['company'] for bus in fetch_all_bus_data(http)['data']]

def fetch_bus_detail(http, bus):
    url = 'http://bus.ke.qq.com/api/cms_detail.php'
    return json.loads(http.request('GET', url, fields={
        '
