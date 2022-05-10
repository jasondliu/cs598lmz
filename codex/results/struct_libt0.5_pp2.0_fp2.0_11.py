import _struct
import sys
import time
import threading
import traceback

from vnpy.trader.vtEvent import *
from vnpy.trader.vtGateway import *
from vnpy.trader.vtFunction import getTempPath
from vnpy.trader.vtObject import VtOrderReq, VtCancelOrderReq, VtSubscribeReq

from .ctpBase import *
from .ctpDataType import *
from .ctpTemplate import CtpTemplate

# 交易接口
class CtpTdApi(TdApi):
    """CTP交易API实现"""

    #----------------------------------------------------------------------
    def __init__(self, gateway):
        """API对象的初始化函数"""
        super(CtpTdApi, self).__init__()
        
        self.gateway = gateway                  # gateway对象
        self.gatewayName = gateway.gatewayName  # gateway对象名
