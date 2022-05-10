import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import pyautogui
from threading import Thread
from tkinter import *
root = Tk()

root.geometry('300x100')
def jess():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    sleep(30)
    def is_alert_present():
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    def close_alert_and_get_its_text(accept_next = True):
        try:
            alert = driver.switch_to_alert()
            alert_text = alert.text
            if accept_next :
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            alert.accept()
   
