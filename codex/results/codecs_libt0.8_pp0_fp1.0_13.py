import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#配置文件路径
INI_PATH = ''

# 查询线路
LINES = {
    '711': u'渝北机场线',
    '715': u'渝北江滨线',

    '517': u'重庆主城线',
    '518': u'渝中渝北线',
    '519': u'北碚主城线',
    '521': u'重庆西南线',
    '522': u'渝北主城外环线',
    '524': u'渝中渝北巴南线',
    '525': u'
