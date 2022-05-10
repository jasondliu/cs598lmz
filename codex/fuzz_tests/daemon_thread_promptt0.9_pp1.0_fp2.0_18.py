import threading
# Test threading daemon argument
    thread = threading.Thread(target = self.write, args = (value))
    thread.daemon = True
    thread.start()
# Test threading daemon argument

######################### OLD CODE ##############################################
    # Set channel frequency
    if channel == 0:
      self._i2cbus.write_byte_data(self._i2caddr, 0x00, 0x34)
      self._i2cbus.write_byte_data(self._i2caddr, 0xFE, 0x00)
      self._i2cbus.write_byte_data(self._i2caddr, 0x00, 0x0C)
    else:
      self._i2cbus.write_byte_data(self._i2caddr, 0x00, 0xB4)
      self._i2cbus.write_byte_data(self._i2caddr, 0xFE, 0x00)
      self._i2cbus.write_byte_data(self._i2caddr, 0x00, 0x8C)


