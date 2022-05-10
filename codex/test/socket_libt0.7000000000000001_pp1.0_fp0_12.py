import socket
import urllib.request
import urllib.parse
import argparse
import requests
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="hostname or IP address", type=str)
    parser.add_argument("--port", help="port number", type=int)
    parser.add_argument("--https", help="use HTTPS", type=int, choices=[0, 1])
    parser.add_argument("--verbose", help="print debugging messages", type=int, choices=[0, 1])
    parser.add_argument("--get", help="GET request", type=int, choices=[0, 1])
    parser.add_argument("--post", help="POST request", type=int, choices=[0, 1])
    parser.add_argument("--data", help="URL encoded data", type=str)
    parser.add_argument("--file", help="file containing data", type=str)
    args = parser.parse_args()

