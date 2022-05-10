import codecs
codecs.register_error('strict', codecs.ignore_errors)


# 取得目前的日期時間
now = datetime.datetime.now()
datestr = now.strftime('%Y%m%d')

# 設定要爬取的查詢網址
url = 'https://www.ettoday.net/news/news-list.htm'

# 設定要存放的資料夾
root_dir = './{}/'.format(datestr)
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

# 取得目前的日期時間
now = datetime.datetime.now()
datestr = now.strftime('%Y%m%d')

# 爬取頁面數
page = 1

# 設定要爬
