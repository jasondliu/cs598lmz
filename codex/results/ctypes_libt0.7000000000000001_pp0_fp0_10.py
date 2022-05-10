import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
But with selenium, I don't know how to do.
Thanks


A:

As you want to pass the text from one textbox to the another textbox you can use the following code block :
<code>from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome('/home/vivek/Downloads/chromedriver')
driver.get("https://www.w3schools.com/html/html_form_input_types.asp")
text=driver.find_element_by_xpath("//input[@name='firstname']").get_attribute("value")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys(text)
</code>

