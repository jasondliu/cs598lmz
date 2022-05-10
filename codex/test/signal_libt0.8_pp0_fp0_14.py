import signal
signal.signal(signal.SIGINT, signal_handler)
    
try:
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = digitalio.DigitalInOut(board.D5)
    rst = digitalio.DigitalInOut(board.D6)
    dc = digitalio.DigitalInOut(board.D26)
except:
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = digitalio.DigitalInOut(board.CE1)
    rst = digitalio.DigitalInOut(board.D25)
    dc = digitalio.DigitalInOut(board.D24)

display = adafruit_st7735.ST7735R(spi, cs=cs, dc=dc, rst=rst, baudrate=10000000, width=128, height=160)

display.fill(0)

bitmap = displayio.Bit
