import threading
threading.stack_size(67108864)

def main():
    coins = CoinMarketCap()
    coins.get_all_coins()
    coins.create_database()
    coins.update_database()
    coins.display_all_coins()
    
    #coins.display_coin_info(coins.get_coin_info(1))
    #coins.display_coin_info_highcharts(coins.get_coin_info(1))
    #coins.display_coin_info_highcharts(coins.get_coin_info(2))
    #coins.display_coin_info_highcharts(coins.get_coin_info(3))
    #coins.display_coin_info_highcharts(coins.get_coin_info(4))
    #coins.display_coin_info_highcharts(coins.get_coin_info(5))
    #coins.display_coin_info_highcharts(coins.get_coin_info(6))
    #coins.display_coin_info_highcharts(coins.get_coin_info(
