import signal
# Test signal.setitimer
# Written by Tim Peters (tim.peters@gmail.com)
#
# Copyright (C) 2002 Python Software Foundation.  All rights reserved.
#
# This file is part of Python.  It is licensed to you under the Python
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
# http://www.python.org/license.
#
# $Id: signal_setitimer_test.py,v 1.1 2002/11/05 21:15:13 akuchling Exp $

import signal
import time
import unittest

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.__alarms = 0
        self.__virtual = 0.0
        self.__prof = 0.0
        self.__oldalrm = signal.signal(signal.SIGALRM, self.alarm)
