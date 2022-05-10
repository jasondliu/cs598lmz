import _struct
from datetime import datetime
from interface import implements
from typing import Dict, Optional, List
from interfaces import IOrder, ITradesAPI, Ticker, OrderType, Trade, OrderSide, \
    OrderStatus, OrderTimeInForce


class BitmexTradesAPI(implements(ITradesAPI)):
    def __init__(self, api_key: str, api_secret: str,
                 base_url: str = "https://www.bitmex.com"):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__base_url = base_url
        self.__session = requests.session()
        self.__session.headers.update({
            "content-type": "application/json",
            "accept": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        })

    def account(self) -> Dict:
        """
        Retrieve the account balance
        :return: Dictionary with the account balance
        """
        return self.__
