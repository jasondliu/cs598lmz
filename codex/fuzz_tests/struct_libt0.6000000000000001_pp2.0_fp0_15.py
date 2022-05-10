import _struct
import binascii
import sys
import time

## This is a script that will be run on an STM32F4Discovery board to control the
## 9DOF board.

## The STM32F4Discovery board has the following pins:
##
## PB6 - LED1
## PB7 - LED2
## PB8 - LED3
## PB9 - LED4
##
## PA0 - ADC0
## PA1 - ADC1
## PA2 - ADC2
## PA3 - ADC3
## PA4 - ADC4
## PA5 - ADC5
## PA6 - ADC6
## PA7 - ADC7
##
## PE9 - BNO055_SCL
## PE10 - BNO055_SDA
## PE11 - BNO055_INT
##
## PB10 - BNO055_RST
##
## PD8 - USB_FS_DP
## PD9 - USB_FS_DM
## PD10 - USB_FS_ID
## PD11 - USB_FS_VBUS
## PD12 - USB_FS_PWR_EN
## PD13
