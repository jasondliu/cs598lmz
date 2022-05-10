import socket
import argparse
import os
import sys

def createOptionParser():
    parser = argparse.ArgumentParser(description="PiCamServer v0.0.1 by mak")
    parser.add_argument("--host", dest="host", default="localhost",
                        help="server is listen on HOST (default: localhost)")
    parser.add_argument("--port", dest="port", type=int, default=2222,
                        help="server is listen on PORT (default: 2222)")
    parser.add_argument("--childprocess", dest="childprocess", action="store_true", default=False,
                        help="control child process")
    parser.add_argument("--no-camera", dest="disablecamera", action="store_true", default=False,
                        help="disable camera")
    parser.add_argument("--no-browser", dest="disablebrowser", action="store_true", default=False,
                        help="disable browser")
