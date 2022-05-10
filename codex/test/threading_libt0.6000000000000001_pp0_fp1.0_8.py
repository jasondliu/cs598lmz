import threading
threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':5000}).start()

# app.run(host='0.0.0.0', port=5000)

# 以下是抓取股票每日数据的脚本
# import tushare as ts
# import pandas as pd
# import datetime

# # 获取当前日期和前一天日期
# today = datetime.datetime.today()
# today_str = today.strftime('%Y-%m-%d')
# yesterday = today - datetime.timedelta(days = 1)
# yesterday_str = yesterday.strftime('%Y-%m-%d')

# # 获取股票代码列表
# stock_list = ts.get_stock_basics()
# stock_list.to_csv('
