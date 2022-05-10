import mmap
import sys, os
import errno
import re
import logging

'''
The goal is read a "stack.txt" and create a series of collapsed stack files
collapsed_nginx_stacks.txt
collapsed_java_stacks.txt
collapsed_kafka_consumer_stacks.txt
collapsed_kafka_producer_stacks.txt
collapsed_other_stacks.txt

Each file will just contain unique stack dumps

wechatapp-oa-service_stacks.txt:
    2020/05/23 13:55:55 [error] 10476#10476: *6124 kevent() reported that connect() returned EAGAIN
    java.net.PlainSocketImpl.socketConnect(Native Method)
    java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:350)
    java.io.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)
    java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:188)
    java.
