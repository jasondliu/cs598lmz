import threading
threading.stack_size(1024*1024)

def get_pairs(exchange):
    pairs = exchange.fetch_markets()
    pairs_list = []
    for pair in pairs:
        pairs_list.append(pair['symbol'])
    return pairs_list

def get_tickers(exchange, pairs):
    tickers = exchange.fetch_tickers()
    tickers_list = []
    for pair in pairs:
        tickers_list.append(tickers[pair]['last'])
    return tickers_list

def get_balances(exchange):
    balances = exchange.fetch_balance()
    balances_list = []
    for balance in balances:
        balances_list.append(balances[balance]['total'])
    return balances_list

def get_order_book(exchange, pair):
    order_book = exchange.fetch_order_book(pair)
    return order_book

def get_trades(exchange, pair):
    trades = exchange.fetch_trades(pair)

