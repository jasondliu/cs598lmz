import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# 初始化
def init():
    global g_RQ_Run, g_RQ_IP, g_RQ_Port, g_RQ_User, g_RQ_Password, g_RQ_AuthCode, g_RQ_ProductInfo, g_RQ_UserProductInfo, g_RQ_StartDate, g_RQ_EndDate
    g_RQ_Run = False
    g_RQ_IP = '127.0.0.1'
    g_RQ_Port = 7709
    g_RQ_User = ''
    g_RQ_Password = ''
    g_RQ_AuthCode = ''
    g_RQ_ProductInfo = '*'
    g_RQ_UserProductInfo = '*'
    g_RQ_StartDate = ''
    g_RQ_EndDate = ''

# 显示回调信
