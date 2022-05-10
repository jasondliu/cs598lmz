import sys, threading

def run():
    sys.argv = ['gw.py', 'runserver', '-h', '0.0.0.0', '-p', '8080']
    from gw import app
    app.run(host='0.0.0.0', port=8080)

t = threading.Thread(target=run)
t.start()

import time
time.sleep(1)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def get_element(driver, id):
    return WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(id))

def get_title(driver):
    return get_element(driver, "title")

def get_text(driver):
    return get_element(driver, "text")

def get_edit_button(driver):
    return get_element(driver, "edit")

def get_save_button(driver):
    return get_element(driver, "save")

def get_cancel_button
