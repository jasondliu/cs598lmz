import _struct
+from pyb import Pin, I2C
+from time import sleep
+from time import time
+from machine import I2C, Pin
+import sys
+
+class MAX30102(object):
+
+	_DEFAULT_I2C_ADDRESS = 0x57
+
+	_INT_STAT1 = 0x00
+	_INT_STAT2 = 0x01
+	_INT_ENABLE1 = 0x02
+	_INT_ENABLE2 = 0x03
+	_FIFO_WR_PTR = 0x04
+	_OVF_COUNTER = 0x05
+	_FIFO_RD_PTR = 0x06
+	_FIFO_DATA = 0x07
+	_FIFO_CONF = 0x08
+	_MODE_CONF = 0x09
+	_SPO2_CONF = 0x0A
+	_LED1_PA = 0x0C
+	_LED2_PA = 0x0D
+	_PILOT_PA
