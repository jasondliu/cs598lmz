import ctypes
import ctypes.util
import threading
import sqlite3
import time
import socket
import random
import logging
import lib.log
import lib.Config
import lib.IpList
import lib.TcpList
import lib.UdpList
import lib.UdpServer
import lib.RadiusList
import lib.RadiusServer
import lib.DhcpList
import lib.DhcpServer
import lib.HttpList
import lib.HttpServer
import lib.SipList
import lib.SipServer
import lib.DnsList
import lib.DnsServer
import lib.SslList
import lib.SslServer
import lib.SmbList
import lib.SmbServer


class Pcap():

    def close(self):
        self.__p.close()

    def set_filter(self, filter):
        self.__p.setfilter(filter)

    def next(self):
        return self.__p.next()

    def loop(self, cnt, callback, arg):
        self.__p.loop(cnt, callback, arg)

    def stats(self):
        return self.__p.
