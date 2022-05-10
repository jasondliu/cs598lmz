import socket
import threading
import time
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import messagebox
from PIL import Image
from tkinter import PhotoImage
from fileprogress import FileProgressBar
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util import Counter
from PIL import ImageTk,Image


class signature(object):
    def make_signature(self,key_path, image_name):
        print(key_path)
        print(image_name)
        in_file = open(key_path, "rb")
        private_key_text = in_file.read()
        in_file.close()
        #print(private_key_text)
        private_key = RSA.importKey(private_key_text)
        h = SHA256.new(image_name)
        signature = private_key.sign(h,'')
        #print(signature)
        return signature

