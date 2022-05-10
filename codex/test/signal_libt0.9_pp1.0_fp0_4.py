import signal
signal.signal(signal.SIGHUP,signal.SIG_IGN)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from tkinter import *
import os

def pompput(event):
    menu.post(event.x_root,event.y_root)

def ikkuna():
    print("ikkuna")

def oliomuokkaus():
    print("oliomuokkaustila")
    
def esikatselu():
    print("esikatselua")
    
def tallenna(event):
    print("tallennetaan...")

def lopeta(event):
    print("suljetaan...")
    exit(0)

def tyhjaa_ikkuna(can):
    can.delete("all")
    
def piirtomerkki(merkki):
    print("merkki")
    
# Juurikansio ja sen alla olevien hakemistojen lukumäärä
root
