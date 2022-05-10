import threading
threading.stack_size(67108864)

def get_data(symbol):
    data = pd.read_csv('data/{}.csv'.format(symbol))
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('data'):
        os.makedirs('data')
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('data/{}.csv'.format(ticker)):
            df =
