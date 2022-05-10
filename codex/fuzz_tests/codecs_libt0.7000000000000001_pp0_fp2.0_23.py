import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def main(date: str = None):
    """
    スクレイピング実行メソッド
    """
    logger = logging.getLogger(__name__)

    if not date:
        date = datetime.date.today()
    params = {
        'appid': os.environ['YAHOO_APP_ID'],
        'date': date.strftime('%Y%m%d')
    }

    logger.info('Yahoo!スポーツのスクレイピングを開始します。')
    logger.info(f'日付：{date.strftime("%Y/%m/%d")}')
    logger.info(f'APIリクエストパラメータ：{params}')

    response = requests.get(
        'https://map.yahooapis.jp/sports/V1/base
