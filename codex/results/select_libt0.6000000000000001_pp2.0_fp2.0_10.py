import select
import socket
import sys
import threading
import time

import os
import os.path

import tftpy

import tests

class TestTftpPacket(tests.TestCase):
    def call(self, *args, **kwargs):
        return tftpy.TftpPacket(*args, **kwargs)

    def test_create(self):
        pkt = self.call('foo', 'bar')
        self.assertEqual(pkt.opcode, 'foo')
        self.assertEqual(pkt.packet, 'bar')

    def test_create_bad_opcode(self):
        self.assertRaises(tftpy.TftpException, self.call, 'badopcode', 'foo')

    def test_pack(self):
        pkt = self.call('DATA', '\x00\x01\x00\x03foo')
        self.assertEqual(pkt.pack(), '\x00\x03\x00\x01foo')

    def test_unpack(self):
       
