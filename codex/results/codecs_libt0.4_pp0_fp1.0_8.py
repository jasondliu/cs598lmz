import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#----------------------------------------------------------------------
def get_stock_data(stock_code, start_date, end_date):
    """"""
    df = ts.get_k_data(stock_code, start=start_date, end=end_date)
    return df

#----------------------------------------------------------------------
def get_stock_data_from_csv(stock_code, start_date, end_date):
    """"""
    df = pd.read_csv(stock_code + '.csv', index_col=0, parse_dates=[0])
    df = df.loc[start_date:end_date]
    return df

#----------------------------------------------------------------------
def get_stock_data_from_csv_with_ma(stock_code, start_date, end_date):
    """"""
    df = pd.read_csv(stock_code + '.csv', index_col=0, parse_dates=[0])
    df = df.loc[start_date:end_
