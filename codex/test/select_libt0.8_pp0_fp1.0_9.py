import select
import sys
import time
import binascii
import argparse

# Define command line argument interface
parser = argparse.ArgumentParser(description='Serial Data Logger')
parser.add_argument('-p','--port', help='Serial port identifier',required=True)
parser.add_argument('-f','--filename',help='Name of output file', required=True)
parser.add_argument('-e','--error',help='Name of error file', required=True)
parser.add_argument('-s','--speed',help='Serial port speed', required=True)
parser.add_argument('-b','--bits',help='Serial port bits', required=True)
parser.add_argument('-q','--parity',help='Serial port parity', required=True)
parser.add_argument('-t','--stopbits',help='Serial port stop bits', required=True)
parser.add_argument('-m','--maxlines',help='Maximum line output in file', required=True)

# Assign args to variables
args = vars(parser.parse_args())
