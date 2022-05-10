import signal
signal.signal(signal.SIGINT, signal_handler)

#Variable Declaration
CURRENCY = 'USD'

def main():
    filename = '{0}.csv'.format(CURRENCY)
    if not os.path.isfile(filename):
        print('Unable to find {0}'.format(filename))
        return

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        markets = [row for row in reader]

    markets = get_delta_time(markets)
    markets = get_buy_price(markets)
    markets = get_sell_price(markets)
    markets = get_arbitrage_profit(markets)
    markets = get_delta_profit_usd(markets)

    if len(markets) == 0:
        print('No arbitrage opportunities found!')
        return

    markets = sorted(markets, key=lambda k: k['delta_profit'], reverse=True)
    print_markets(markets)

