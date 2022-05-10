import threading
# Test threading daemon
import subprocess
# Test subprocess


CASE_PASSED = 0x01
CASE_FAILED = 0xFF

exit_code = 0

GPIO_LED = 'gpio_led'
LED_PATH = '/sys/class/leds/beaglebone:green:usr'
LED_PATH_0 = LED_PATH + '0'
LED_PATH_1 = LED_PATH + '1'
LED_PATH_2 = LED_PATH + '2'
LED_PATH_3 = LED_PATH + '3'
LED_TRIGGER = LED_PATH + '/trigger'
LED_BRIGHTNESS = LED_PATH + '/brightness'

GPIO_BUTTON = 'gpio_button'
BUTTON_PATH = '/sys/class/gpio/gpio'
BUTTON_PATH_68 = BUTTON_PATH + '68'
BUTTON_PATH_44 = BUTTON_PATH + '44'
BUTTON_PATH_23 = BUTTON_PATH + '23'
BUTTON_PATH_26 = BUTTON_PATH + '26'

GPIO
